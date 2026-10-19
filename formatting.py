"""Средства текстового представления результатов сортировки."""


def format_result(name, original, sorted_values):
    return f'{name}: {list(original)} -> {list(sorted_values)}'


def format_comparison(name, values):
    return f'{name}: {len(list(values))} элементов'
