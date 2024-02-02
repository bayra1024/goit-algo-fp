import random
import matplotlib.pyplot as plt
import numpy as np


# Функція для симуляції кидання двох кубиків
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


# Кількість кидків у симуляції
num_rolls = 100000

# Словник для зберігання кількості разів, коли кожна сума випала
sum_counts = {i: 0 for i in range(2, 13)}

# Виконуємо симуляцію
for _ in range(num_rolls):
    total = roll_dice()
    sum_counts[total] += 1

# Обчислюємо імовірності методом Монте-Карло
monte_carlo_probabilities = {
    key: value / num_rolls * 100 for key, value in sum_counts.items()
}

# Аналітичні імовірності
analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

# Створюємо графік
plt.bar(
    monte_carlo_probabilities.keys(),
    monte_carlo_probabilities.values(),
    color="#00ff00",
    alpha=0.5,
    label="Метод Монте-Карло",
)
plt.scatter(
    analytical_probabilities.keys(),
    analytical_probabilities.values(),
    color="#ff00ff",
    label="Аналітичний розрахунок",
)
x = np.array(list(analytical_probabilities.keys()))
y = np.array(list(analytical_probabilities.values()))
plt.plot(x, y, "-o", color="#ff00ff", linestyle="dashed")
plt.title("Порівняння імовірностей сум при киданні двох кубиків")
plt.xlabel("Сума")
plt.ylabel("Імовірність, %")
plt.legend()
plt.show()
