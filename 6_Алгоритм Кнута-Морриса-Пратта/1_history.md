## История алгоритма Кнута — Морриса — Пратта

В 1960-х годах компьютерные науки переживали бум: текстовые редакторы стали обычным инструментом, и программисты столкнулись с проблемой — как быстро находить подстроки в больших текстах? Наивный поиск (посимвольное сравнение) работал медленно, особенно на больших данных.

В 1967 году два американских учёных — Дональд Кнут и Воган Прат — независимо друг от друга начали исследовать эту задачу. Кнут, уже известный по работе над "Искусством программирования", искал способы ускорения обработки текста. Пратт, специалист по теории вычислений, изучал формальные языки и автоматы.

Позже к ним присоединился Джеймс Моррис, инженер из Bell Labs, который работал над похожей проблемой в системах поиска. Втроём они объединили идеи префикс-функций и частичных совпадений, что привело к созданию алгоритма, который избегал лишних сравнений за счёт предварительного анализа искомой строки.

Алгоритм KMP был впервые опубликован в 1977 году и произвёл революцию в строковом поиске. Его ключевая идея — использование частичного совпадения для сдвига шаблона без возврата в тексте — сделала его в разы быстрее наивного подхода.

Сегодня KMP лежит в основе многих поисковых систем, редакторов и даже биоинформатических алгоритмов, доказывая, что даже задачи, кажущиеся простыми, могут иметь изящные и мощные решения.
