"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""


def colors(amount, **kwargs):
    print(f'Цвета: {amount}')
    for color,number in kwargs.items():
        print(f'{color}: {number}')

amount = int(input('Кол-во цветов: '))
colors(amount, цвет1 = 1, цвет2 = 5, цвет3 = 9)