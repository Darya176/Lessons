string = str(input('Введите номер:'))
a = string.replace(' ', '')
b = a.replace('-', '')
c = b.replace('(', '')
d = c.replace(')', '')
f = d.replace('+', '')
print(f)