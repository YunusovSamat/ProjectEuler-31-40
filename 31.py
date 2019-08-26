"""
------------------------------- Задание -------------------------------
В Англии валютой являются фунты стерлингов £ и пенсы p, и в обращении
есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Сколькими разными способами можно составить £2, используя любое
количество монет?
"""

# coins_all = [100, 50, 20, 10, 5, 2, 1]
coins_all = [5, 2, 1]


def coin_tree(coins, sum_coins, sequence):
    if sum_coins + coins[0] < limit:
        if limit - sum_coins - coins[0] >= coins[0]:
            coin_tree(coins, sum_coins + coins[0], sequence+str(coins[0]))
        else:
            coin_tree(coins[1:], sum_coins+coins[0], sequence+str(coins[0]))
    elif sum_coins + coins[0] == limit:
        print(sequence + str(coins[0]))
    #     combinations += 1

    for coin in coins[1:]:
        if sum_coins + coin < limit:
            coin_tree(coins[coins.index(coin):], sum_coins+coin, sequence+str(coin))
        elif sum_coins + coin == limit:
            print(sequence+str(coin))
            # global combinations
            # combinations += 1


if __name__ == '__main__':
    limit = 10
    combinations = 0
    coin_tree(coins_all, 0, '')
    # print(combinations)
