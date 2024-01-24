# Задача No1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для сортировки
# числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers: list) -> list:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


print(sort_list_imperative([22, 39, 10, 8, 56, 12, 2, 291]))
