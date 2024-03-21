import csv

with open('scientist.txt', encoding='utf8') as f:
    # создадим список словарей с именами, датами и тд
    reader = list(csv.DictReader(f, delimiter='#', quotechar= '"'))
    data = sorted(reader, key=lambda x: x['date'])
for el in data:
    print(el)