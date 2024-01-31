# Задача:
# Написать программу на любом языке в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число. На выходе - индекс
# элемента или - 1, в случае если искомого элемента нет в массиве.


def binary_search(elem, arr):
    head = 0
    tail = len(arr) - 1

    while head <= tail:
        mid_index = (head + tail) // 2
        mid_value = arr[mid_index]

        if mid_value == elem:
            return mid_index
        elif mid_value < elem:
            head = mid_index + 1
        else:
            tail = mid_index - 1

    return -1


elem = 365
arr = [2, 8, 10, 12, 22, 39, 56, 291, 365]
print(binary_search(elem, arr))
