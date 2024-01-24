# Задача No2
# Написать точно такую же процедуру, но в декларативном стиле.

def sort_list_declarative(numbers: list) -> list:
    return sorted(numbers, reverse=True)


print(sort_list_declarative([22, 39, 10, 8, 56, 12, 2, 291]))
