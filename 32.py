"""
------------------------------- Задание -------------------------------
Каждое n-значное число, которое содержит каждую цифру от 1 до n ровно
один раз, будем считать пан-цифровым; к примеру, 5-значное число 15234
является пан-цифровым, т.к. содержит цифры от 1 до 5.

Произведение 7254 является необычным, поскольку равенство
39 × 186 = 7254, состоящее из множимого, множителя и произведения
является пан-цифровым, т.е. содержит цифры от 1 до 9.

Найдите сумму всех пан-цифровых произведений, для которых равенство
"множимое × множитель = произведение" можно записать цифрами
от 1 до 9, используя каждую цифру только один раз.

ПОДСКАЗКА: Некоторые произведения можно получить несколькими
способами, поэтому убедитесь, что включили их в сумму лишь единожды.
"""


class PandigitalProducts:
    def __init__(self):
        self._all_pandigital_products = set()
        self._multi_range = [
            {
                'm-cand_bgn': 1, 'm-cand_end': 10,
                'm-er_bgn': 1000, 'm-er_end': 10000
            },
            {
                'm-cand_bgn': 10, 'm-cand_end': 100,
                'm-er_bgn': 100, 'm-er_end': 1000
            }]

    def sum_pandigital_products(self):
        for multi in self._multi_range:
            for multiplicand in range(multi['m-cand_bgn'], multi['m-cand_end']):
                for multiplier in range(multi['m-er_bgn'], multi['m-er_end']):
                    all_numbers = (str(multiplicand) + str(multiplier) +
                                   str(multiplicand*multiplier))
                    if len(all_numbers) > 9:
                        break
                    elif len(all_numbers) == 9:
                        if sorted(all_numbers) == list('123456789'):
                            self._all_pandigital_products.add(multiplicand*multiplier)
        return sum(self._all_pandigital_products)


if __name__ == '__main__':
    pandigital_products = PandigitalProducts()
    print(__doc__)
    print('Ответ:', pandigital_products.sum_pandigital_products())
