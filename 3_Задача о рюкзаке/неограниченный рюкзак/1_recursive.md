## Рекурсивный метод

Задача разбивается на подзадачи.

Для каждого предмета мы решаем:
1. Взять его (и продолжить рекурсию с уменьшенной вместимостью capacity - weight[i]).
2. Не брать его (перейти к следующему предмету).
3. Сохраняем уже вычисленные результаты, чтобы избежать повторных вычислений.
