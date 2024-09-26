import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

# Функція для симуляції багатьох кидків
def monte_carlo_simulation(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}  # Від 2 до 12

    for _ in range(num_rolls):
        die1, die2 = roll_dice()
        dice_sum = die1 + die2
        sums_count[dice_sum] += 1

    # Обчислюємо ймовірності
    probabilities = {k: v / num_rolls for k, v in sums_count.items()}
    return probabilities

# Аналітичні ймовірності (з таблиці)
analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Симуляція методом Монте-Карло
num_rolls = 1000000  # Велика кількість кидків для точності
monte_carlo_probabilities = monte_carlo_simulation(num_rolls)

# Порівняння результатів
print("Ймовірності методом Монте-Карло:")
for sum_value, probability in monte_carlo_probabilities.items():
    print(f"Сума {sum_value}: {probability:.4%}")

# Побудова графіку
sums = list(monte_carlo_probabilities.keys())
mc_probs = list(monte_carlo_probabilities.values())
analytical_probs = [analytical_probabilities[sum_val] for sum_val in sums]

plt.plot(sums, mc_probs, 'o-', label='Монте-Карло', color='blue')
plt.plot(sums, analytical_probs, 's-', label='Аналітичні', color='red')

plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум при киданні двох кубиків: Монте-Карло vs Аналітичні')
plt.legend()
plt.grid(True)
plt.show()