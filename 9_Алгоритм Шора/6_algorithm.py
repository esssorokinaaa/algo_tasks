import math
import random
from fractions import Fraction
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT

def shor_algorithm(N):
    """Основная функция алгоритма Шора"""
    
    # 1. Проверка простых случаев
    if N % 2 == 0:
        return 2
    if is_power(N):
        return is_power(N)
    
    # 2. Подготовка случайного основания
    a = random.randint(2, N-1)
    gcd = math.gcd(a, N)
    if gcd != 1:
        return gcd
    
    # 3. Квантовая часть - поиск периода
    t = 2 * N.bit_length()  # Число кубитов для точности
    qc = create_quantum_circuit(a, N, t)
    
    # 4. Запуск на симуляторе (в реальности - квантовый компьютер)
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts()
    
    # 5. Постобработка результатов
    measured_value = max(counts.items(), key=lambda x: x[1])[0]
    r = find_period(int(measured_value, 2), t, N)
    
    # 6. Проверка и возврат результата
    if r is not None and r % 2 == 0:
        factor1 = math.gcd(a**(r//2) - 1, N)
        factor2 = math.gcd(a**(r//2) + 1, N)
        if factor1 not in [1, N]:
            return factor1
        if factor2 not in [1, N]:
            return factor2
    return None

def create_quantum_circuit(a, N, t):
    """Создаем квантовую схему для поиска периода"""
    n = N.bit_length()
    qc = QuantumCircuit(t + 2*n, t)  # t кубитов для оценки, 2n для вычислений
    
    # 1. Инициализация суперпозиции
    qc.h(range(t))
    
    # 2. Добавляем |1⟩ во второй регистр
    qc.x(t + n)
    
    # 3. Применяем модульную экспоненту
    for q in range(t):
        exponent = 2**q
        qc.append(controlled_U(a, exponent, N, n), 
                 [q] + list(range(t, t + 2*n)))
    
    # 4. Применяем обратное QFT
    qc.append(QFT(t, inverse=True), range(t))
    
    # 5. Измеряем первые t кубитов
    qc.measure(range(t), range(t))
    
    return qc

def controlled_U(a, power, N, n):
    """Контролируемая операция U: |x⟩|y⟩ → |x⟩|y + a^x mod N⟩"""
    U = QuantumCircuit(2*n)
    
    # Упрощенная реализация для демонстрации
    # В реальности это сложная квантовая схема
    for _ in range(power):
        U.swap(0, 1)  # Заглушка для реальной операции
        U.cp(2*math.pi/N, 0, 1)
    
    U = U.to_gate()
    U.name = f"{a}^{power} mod {N}"
    return U

def find_period(measurement, t, N):
    """Находим период через цепные дроби"""
    phase = measurement / 2**t
    frac = Fraction(phase).limit_denominator(N)
    r = frac.denominator
    
    # Проверяем, что это действительно период
    if pow(a, r, N) == 1:
        return r
    return None

def is_power(n):
    """Проверяем, является ли число степенью"""
    for b in range(2, int(math.log2(n)) + 1):
        a = n ** (1/b)
        if a.is_integer():
            return int(a)
    return None

number_to_factor = 15
factor = shor_algorithm(number_to_factor)
print(f"Один из множителей {number_to_factor}: {factor}")
