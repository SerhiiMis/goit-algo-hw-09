def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізуємо масив для зберігання мінімальної кількості монет для кожної суми від 0 до amount
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для суми 0 потрібно 0 монет

    # Ініціалізуємо масив для зберігання останньої монети, використаної для кожної суми
    coin_used = [0] * (amount + 1)

    # Динамічне програмування для заповнення масиву min_coins
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin

    # Відновлюємо набір монет із масиву coin_used
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

# Приклад використання
print(find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}