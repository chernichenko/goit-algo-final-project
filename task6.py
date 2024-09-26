# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if info["cost"] <= budget:
            chosen_items.append(item)
            total_calories += info["calories"]
            budget -= info["cost"]
    
    return chosen_items, total_calories

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    # Ініціалізуємо таблицю для зберігання результатів
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        item_name, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]
        
        for w in range(1, budget + 1):
            if cost <= w:
                # Вибираємо максимум між взяттям поточного продукту або ігноруванням його
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відтворюємо набір вибраних продуктів
    chosen_items = []
    total_calories = dp[n][budget]
    w = budget
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = item_list[i - 1][0]
            chosen_items.append(item_name)
            w -= item_list[i - 1][1]["cost"]
    
    return chosen_items, total_calories

# Тестування з бюджетом
budget = 100

# Використання жадібного алгоритму
greedy_items, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_items)
print("Загальна калорійність:", greedy_calories)

# Використання алгоритму динамічного програмування
dp_items, dp_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", dp_items)
print("Загальна калорійність:", dp_calories)