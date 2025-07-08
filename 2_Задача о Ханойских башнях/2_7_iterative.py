def hanoi_iterative(n, source, target, auxiliary):
    stack = [(n, source, target, auxiliary, False)]  # Создаем стек с начальной задачей
    
    while stack:
        num, src, tgt, aux, processed = stack.pop()  # Берем последнюю задачу
        
        if num == 1:  # Если остался один диск - просто переносим
            print(f"Переносим диск 1 с {src} на {tgt}")
        elif not processed:  # Если задача еще не обрабатывалась
            # Кладем задачи в стек в обратном порядке выполнения:
            stack.append((num, src, tgt, aux, True))  # Помечаем как обработанную
            stack.append((num-1, aux, tgt, src, False))  # Шаг 3 (будет выполняться последним)
            stack.append((1, src, tgt, aux, False))  # Шаг 2 (перенос самого большого диска)
            stack.append((num-1, src, aux, tgt, False))  # Шаг 1 (будет выполняться первым)
