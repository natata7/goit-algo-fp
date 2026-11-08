import random
import matplotlib.pyplot as plt

THEORETICAL = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def simulate_dice_rolls(num_trials: int = 1_000_000):
    counts = {sum_val: 0 for sum_val in range(2, 13)}

    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        counts[dice_sum] += 1

    return counts


def display_comparison_table(counts: dict, num_trials: int):
    print(
        f"{'Сума':<6} | {'Кількість':<12} | {'Монте-Карло (%)':<18} | {'Теоретична (%)':<18} | {'Різниця (%)':<10}"
    )

    for sum_val in range(2, 13):
        mc_prob = (counts[sum_val] / num_trials) * 100
        theo_prob = THEORETICAL[sum_val] * 100
        diff = abs(mc_prob - theo_prob)

        print(
            f"{sum_val:<6} | {counts[sum_val]:<12} | {mc_prob:<18.2f} | {theo_prob:<18.2f} | {diff:<10.2f}"
        )


def plot_results(counts: dict, num_trials: int):
    sums = list(range(2, 13))
    mc_probs = [(counts[s] / num_trials) * 100 for s in sums]
    theo_probs = [THEORETICAL[s] * 100 for s in sums]

    x = list(range(len(sums)))
    width = 0.35

    plt.figure(figsize=(10, 6))

    plt.bar(
        [i - width / 2 for i in x],
        mc_probs,
        width,
        label="Монте-Карло",
        color="#1f77b4",
        alpha=0.85,
    )
    plt.bar(
        [i + width / 2 for i in x],
        theo_probs,
        width,
        label="Аналітичні",
        color="#ff7f0e",
        alpha=0.85,
    )

    plt.xlabel("Сума кидку на двох кубиках", fontsize=12)
    plt.ylabel("Імовірність", fontsize=12)
    plt.title(
        f"Порівняння ймовірностей сум при {num_trials:,} кидках кубиків",
        fontsize=14,
        pad=15,
    )
    plt.xticks(x, sums)
    plt.legend(fontsize=11)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    NUM_TRIALS = 1_000_000
    print(f"Запуск симуляції Монте-Карло для {NUM_TRIALS:,} кидків...")

    counts = simulate_dice_rolls(NUM_TRIALS)
    display_comparison_table(counts, NUM_TRIALS)
    plot_results(counts, NUM_TRIALS)
