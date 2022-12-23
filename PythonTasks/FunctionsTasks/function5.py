"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""

def print_awards():

    while True:
        start = input('Введите "старт" для запуска программы или "стоп" для завершения работы: ')
        if start == 'стоп':
            print('Список составлен')
            break
        else:
            name = input('Имя студента: ')
            amount = int(input('Число предметов: '))
            list = []
            for i in range(amount):
                i = int(input('Баллы: '))
                if i <=0 or i >50:
                    print(i, 'балл некорректен, в итоговом счете не учитывается')
                else:
                    list.append(i)
            summa = sum(list)
            print('Итоговый счет:', summa)
            if summa >80:
                print('Наградить дипломом.')
            elif summa >50 and summa <=80:
                print('Наградить похвальной грамотой.')
            else:
                print('Выдать грамоту об участии.')


print_awards()








