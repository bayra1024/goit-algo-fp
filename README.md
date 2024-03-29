#### goit-algo-fp

#### **Висновки моделювання кидання двох ігрових кубиків:**

Аналітичні імовірності можна розрахувати, використовуючи всі можливі комбінації чисел, які можуть випасти на двох кубиках. Загальна кількість можливих комбінацій - 6 * 6 = 36 (оскільки на кожному кубику є 6 граней).

Тепер розрахуємо імовірність для кожної суми:


| Сума | Спосіб (Комбінація) | Ймовірність |
|------|----------------------|--------------|
| 2    | 1 + 1                | 1/36         |
| 3    | 1 + 2, 2 + 1          | 2/36         |
| 4    | 1 + 3, 2 + 2, 3 + 1    | 3/36         |
| 5    | 1 + 4, 2 + 3, 3 + 2, 4 + 1 | 4/36     |
| 6    | 1 + 5, 2 + 4, 3 + 3, 4 + 2, 5 + 1 | 5/36 |
| 7    | 1 + 6, 2 + 5, 3 + 4, 4 + 3, 5 + 2, 6 + 1 | 6/36 |
| 8    | 2 + 6, 3 + 5, 4 + 4, 5 + 3, 6 + 2 | 5/36 |
| 9    | 3 + 6, 4 + 5, 5 + 4, 6 + 3 | 4/36       |
| 10   | 4 + 6, 5 + 5, 6 + 4      | 3/36       |
| 11   | 5 + 6, 6 + 5             | 2/36       |
| 12   | 6 + 6                   | 1/36       |



Імовірності (Метод Монте-Карло):
| Сума | Імовірність |
|------|-------------|
| 2    | 2.69%       |
| 3    | 5.47%       |
| 4    | 8.30%       |
| 5    | 11.07%      |
| 6    | 14.05%      |
| 7    | 16.73%      |
| 8    | 13.87%      |
| 9    | 11.17%      |
| 10   | 8.22%       |
| 11   | 5.53%       |
| 12   | 2.90%       |


