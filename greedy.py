COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int) -> dict:
    result = {}
    for coin in COINS:
        if amount <= 0:
            break
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count
    return result

if __name__ == '__main__':
    amount = 123
    print(find_coins_greedy(amount))