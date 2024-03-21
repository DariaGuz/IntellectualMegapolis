import csv

with open('scientist.txt', encoding='utf8') as f:
    # создадим список словарей с именами, датами и тд
    reader = list(csv.DictReader(f, delimiter='#', quotechar= '"'))
    # отсортируем список по датам
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while reader[j]['date'] < key['date'] and j >= 0:
            reader[j + 1] = reader[j]
            j -= 1
        reader[j+1] = key


# выведем пять самых ранних препаратов
count = 1
for el in reader:
    if count != 6:
        print(el['ScientistName'] + ': ' + el['preparation'])
        count += 1
    else:
        break