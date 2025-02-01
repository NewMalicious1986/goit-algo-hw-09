COINS = [50, 25, 10, 5, 2, 1]

def find_min_coins(amount: int) -> dict:

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    last_coin = [None] * (amount + 1)

    for a in range(1, amount + 1):
        for coin in COINS:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                last_coin[a] = coin

    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


if __name__ == '__main__':
    amount = 123
    print(find_min_coins(amount))