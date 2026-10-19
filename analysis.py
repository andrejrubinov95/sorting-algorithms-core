"""Дополнительная статистика для алгоритмов сортировки."""


def count_inversions(values):
    """Число пар элементов, расположенных не по возрастанию."""
    data = list(values)
    return sum(data[i] > data[j] for i in range(len(data)) for j in range(i + 1, len(data)))


def is_sorted(values):
    """Проверяет неубывающий порядок элементов."""
    data = list(values)
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))
