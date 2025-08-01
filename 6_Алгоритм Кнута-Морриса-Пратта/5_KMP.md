## Алгоритма Кнута-Морриса-Пратта (KMP)

Алгоритм KMP решает проблему избыточных сравнений в наивном подходе, используя ключевую концепцию: 
> "При обнаружении несовпадения, образец можно сдвинуть не на 1 символ, а на заранее вычисленное максимально возможное расстояние"

**Префикс-функция (LPS)**

LPS - наибольший собственный префикс, являющийся суффиксом

**Что хранит LPS-таблица?**
Для каждой позиции i в образце P - длину максимального совпадающего префикса и суффикса для подстроки P[0..i]

**Как вычисляется LPS?**
1. Инициализируем lps[0] = 0 (у односимвольной строки нет префиксов/суффиксов)
2. Используем два указателя:
   - len = 0 (длина текущего совпадения)
   - i = 1 (текущая позиция в образце)
