
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


class CombinationsCoins:
    def __init__(self, limit=200, coins_all=None):
        if coins_all is None:
            coins_all = [200, 100, 50, 20, 10, 5, 2, 1]
        self._coins_all = coins_all
        self._combinations = 0
        self._limit = limit
        self.coin_tree(self._coins_all, 0)

    def coin_tree(self, coins, sum_coins):
        if coins[0] == 1:
            self._combinations += 1
        elif sum_coins + coins[0] < self._limit:
            if self._limit - sum_coins - coins[0] >= coins[0]:
                self.coin_tree(coins, sum_coins+coins[0])
            else:
                self.coin_tree(coins[1:], sum_coins+coins[0])
        elif sum_coins + coins[0] == self._limit:
            self._combinations += 1

        for i, coin in enumerate(coins[1:]):
            if sum_coins + coin < self._limit:
                self.coin_tree(coins[i+1:], sum_coins+coin)
            elif sum_coins + coin == self._limit:
                self._combinations += 1

    def get_combinations(self):
        return self._combinations


if __name__ == '__main__':
    combinations_coins = CombinationsCoins()
    print('Ответ:', combinations_coins.get_combinations())
