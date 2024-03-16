import csv

alph = sorted('ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
d = {alph[i]: i + 1 for i in range(len(alph))}

def cassh(s):
    p = 67
    m = 10 ** 9 + 9
    cash_value = 0
    i = 0
    for cash in s:
        cash_value += d[cash] * p ** i
        i += 1
    return int(cash_value % m)

with open('vacancy.csv', encoding='utf-8') as file, open('vacancy_with_cash', 'w', encoding='utf-8', newline='') as new_file:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(new_file, delimiter=';')

