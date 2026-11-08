items = {
  "pizza": {"cost": 50, "calories": 300},
  "hamburger": {"cost": 40, "calories": 250},
  "hot-dog": {"cost": 30, "calories": 200},
  "pepsi": {"cost": 10, "calories": 100},
  "cola": {"cost": 15, "calories": 220},
  "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items: dict, budget: int) -> tuple[list[str], int, int]:
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, info in sorted_items:
        cost = info["cost"]
        calories = info["calories"]

        if total_cost + cost <= budget:
            selected_items.append(item_name)
            total_cost += cost
            total_calories += calories

    return selected_items, total_cost, total_calories


def dynamic_programming(items: dict, budget: int) -> tuple[list[str], int, int]:
    item_names = list(items.keys())
    n = len(item_names)

    table = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                table[i][b] = max(table[i - 1][b], table[i - 1][b - cost] + calories)
            else:
                table[i][b] = table[i - 1][b]

    selected_items = []
    remaining_budget = budget
    for i in range(n, 0, -1):
        b = remaining_budget
        if table[i][b] != table[i - 1][b]:
            name = item_names[i - 1]
            selected_items.append(name)
            remaining_budget -= items[name]["cost"]

    selected_items.reverse()
    total_calories = table[n][budget]
    total_cost = sum(items[name]["cost"] for name in selected_items)

    return selected_items, total_cost, total_calories

if __name__ == "__main__":
    test_budget = 50

    print(f"Початковий бюджет: {test_budget} грн\n")

    g_items, g_cost, g_cal = greedy_algorithm(items, test_budget)
    print("Жадібний алгоритм")
    print(f"Обрані страви: {g_items}")
    print(f"Витрачено бюджету: {g_cost} грн")
    print(f"Сумарна калорійність: {g_cal} ккал\n")

    dp_items, dp_cost, dp_cal = dynamic_programming(items, test_budget)
    print("Динамічне програмування")
    print(f"Обрані страви: {dp_items}")
    print(f"Витрачено бюджету: {dp_cost} грн")
    print(f"Сумарна калорійність: {dp_cal} ккал")