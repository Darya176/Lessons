"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""


dictionary = {'one': 1,
              'two': 2,
              'three': 3,
              'four': 4,
              'five': 5}
print(dictionary)
dictionary.update({'one': '5', 'five': '1'})
del dictionary['two']
dictionary['six'] = '6'
print(dictionary)