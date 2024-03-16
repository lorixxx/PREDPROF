import csv

with (open('vacancy.csv', encoding='utf-8') as file, open('vacancy_new.csv', 'w', encoding='utf-8', newline='') as new_file):
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(new_file, delimiter=';')

    a = []
    b = []
    s = ''
    for i in data[1:]:
        a.append(int(i[0]))
    # print(a)
    r1 = max(a)
    while r1 in a:
        for i in a:
            if i == r1:
                a.remove(i)
    r2 = max(a)
    while r2 in a:
        for i in a:
            if i == r2:
                a.remove(i)
    r3 = max(a)
    while r3 in a:
        for i in a:
            if i == r3:
                a.remove(i)
    zp1 = str(r1)
    zp2 = str(r2)
    zp3 = str(r3)
    m = 1
    for stroka in data[1:]:
        if zp1 in stroka or zp2 in stroka or zp3 in stroka:
            print(f'{stroka[4]} - {stroka[3]} - {stroka[0]}')
            m+=1
            if m == 4:
                break
