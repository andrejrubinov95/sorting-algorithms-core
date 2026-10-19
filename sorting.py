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


def selection_sort(values):
    """Сортировка выбором; возвращает новый список."""
    data = list(values)
    for i in range(len(data)):
        minimum = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[minimum] = data[minimum], data[i]
    return data


def cocktail_sort(values):
    """Двусторонняя сортировка пузырьком (шейкерная)."""
    data = list(values)
    left, right = 0, len(data) - 1
    while left < right:
        swapped = False
        for i in range(left, right):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        right -= 1
        for i in range(right, left, -1):
            if data[i - 1] > data[i]:
                data[i], data[i - 1] = data[i - 1], data[i]
                swapped = True
        left += 1
        if not swapped:
            break
    return data
