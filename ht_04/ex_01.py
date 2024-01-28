# Задача:
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
# Можете использовать любую парадигму, но рекомендую использовать функциональную,
# т.к. в этом примере она значительно упростит вам жизнь.

import math


def correlation(data_x: list[int], data_y: list[int]) -> int | float:
    # r_xy = sum((x_i - M_x) * (y_i - M_y)) / sqrt(sum((x_i - M_x) ** 2 * (y_i - M_y) ** 2))
    M_x = sum(data_x) / len(data_x)
    M_y = sum(data_y) / len(data_y)

    def numerator(x, y):
        return (x - M_x) * (y - M_y)

    numer = sum(map(numerator, data_x, data_y))
    denom = math.sqrt(sum(map(lambda x: (x - M_x) ** 2, data_x)) *
                      sum(map(lambda x: (x - M_y) ** 2, data_y)))

    return numer/denom if denom != 0 else 0


data_x = [i for i in range(1, 10)]
data_y = [i for i in range(1, 20, 2)]
r_xy = correlation(data_x, data_y)

print(r_xy)
