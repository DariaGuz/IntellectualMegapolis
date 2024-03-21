import csv

with open('scientist.txt', encoding='utf8') as f:
    reader = list(csv.DictReader(f, delimiter='#', quotechar= '"'))
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while float(reader[j]['date'] if reader[j]['date'] != )