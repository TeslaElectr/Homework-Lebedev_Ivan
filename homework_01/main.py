"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: x ** 2, numbers))
    # return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_odd(number):
    if number % 2:
        return True
    else:
        return False


def filter_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


def filter_prime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for item in range(3, int(number ** 0.5) + 1, 2):
        if not number % item:
            return False
    return True


def filter_numbers(numbers_list: list, filter_type: str):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD:
        return list(filter(filter_odd, numbers_list))
    elif filter_type == EVEN:
        return list(filter(filter_even, numbers_list))
    elif filter_type == PRIME:
        return list(filter(filter_prime, numbers_list))

