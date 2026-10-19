"""Библиотека алгоритмов сортировки. Версия 1: пузырёк и вставки."""


def bubble_sort(values):
    """Сортировка пузырьком; исходный список не изменяется."""
    data = list(values)
    for last in range(len(data) - 1, 0, -1):
        swapped = False
        for pos in range(last):
            if data[pos] > data[pos + 1]:
                data[pos], data[pos + 1] = data[pos + 1], data[pos]
                swapped = True
        if not swapped:
            break
    return data


def insertion_sort(values):
    """Сортировка вставками; исходный список не изменяется."""
    data = list(values)
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and data[j] > current:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current
    return data
