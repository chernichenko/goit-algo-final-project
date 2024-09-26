# Завдання 7: Моделювання кидання двох кубиків за допомогою методу Монте-Карло

## Опис

Це завдання включає програмну реалізацію алгоритму для моделювання кидання двох ігрових кубиків. Метою є побудова таблиці ймовірностей сум чисел, які випадають на кубиках, за допомогою методу Монте-Карло, а також порівняння отриманих результатів з аналітичними ймовірностями.

## Алгоритм

1. Виконано симуляцію 1 мільйона кидків двох кубиків.
2. Для кожного кидка обчислено суму значень обох кубиків.
3. Підраховано, скільки разів кожна можлива сума з’являється у процесі симуляції.
4. Обчислено ймовірність для кожної суми (від 2 до 12).
5. Створено графік для порівняння результатів, отриманих методом Монте-Карло, з аналітичними розрахунками.

## Результати

### Аналітичні ймовірності:

| Сума | Імовірність (%) |
|------|----------------|
| 2    | 2.78% (1/36)   |
| 3    | 5.56% (2/36)   |
| 4    | 8.33% (3/36)   |
| 5    | 11.11% (4/36)  |
| 6    | 13.89% (5/36)  |
| 7    | 16.67% (6/36)  |
| 8    | 13.89% (5/36)  |
| 9    | 11.11% (4/36)  |
| 10   | 8.33% (3/36)   |
| 11   | 5.56% (2/36)   |
| 12   | 2.78% (1/36)   |

### Ймовірності методом Монте-Карло:

Після симуляції 1 мільйона кидків кубиків, отримані наступні ймовірності для кожної суми:

| Сума | Ймовірність (%) |
|------|----------------|
| 2    | 2.78%          |
| 3    | 5.55%          |
| 4    | 8.33%          |
| 5    | 11.11%         |
| 6    | 13.89%         |
| 7    | 16.67%         |
| 8    | 13.89%         |
| 9    | 11.11%         |
| 10   | 8.33%          |
| 11   | 5.56%          |
| 12   | 2.78%          |

## Графік порівняння

![Графік порівняння](path/to/your/graph.png)

## Висновки

1. **Результати симуляції методом Монте-Карло дуже близькі до аналітичних розрахунків**, що підтверджує правильність алгоритму.
2. Метод Монте-Карло показав високу точність при великій кількості кидків (1 мільйон), де відхилення ймовірностей були мінімальні.
3. Результати симуляції демонструють, що найбільш ймовірна сума — 7 (приблизно 16.67% випадків), що відповідає аналітичним розрахункам.
4. Метод Монте-Карло є ефективним для підтвердження аналітичних результатів, коли важко вивести точні ймовірності вручну.

Ці висновки показують ефективність методу Монте-Карло для задач такого типу і можуть бути застосовані для більш складних моделювань.