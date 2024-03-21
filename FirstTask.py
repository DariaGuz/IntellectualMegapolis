import csv

with open('scientist.txt', encoding='utf8') as f:
    # создадим список словарей с именами, датами и тд
    reader = list(csv.DictReader(f, delimiter='#', quotechar= '"'))
    # отсортируем список по датам
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while reader[j]['date'] > key['date'] and j >= 0:
            reader[j + 1] = reader[j]
            j -= 1
        reader[j + 1] = key

# создадим новый словарь, куда будем записывать настоящих создателей
new_slovar = {'ScientistName': [], 'preparation': [], 'date': [], 'components': []}
# создадим словарь подельникова Аллопуринола
lst_robbers = {'ScientistName': [], 'date': []}
for el in reader:
    name = el['ScientistName']
    prep = el['preparation']
    date = el['date']
    comp = el['components']
    if prep == 'Аллопуринол':
        lst_robbers['ScientistName'].append(name)
        lst_robbers['date'].append(date)
        continue
    if name not in new_slovar['ScientistName']:
        new_slovar['ScientistName'].append(name)
        new_slovar['preparation'].append(prep)
        new_slovar['date'].append(date)
        new_slovar['components'].append(comp)

print('Разработчиками Аллопуринола были такие люди:')
for i in range(1, len(lst_robbers['ScientistName'])):
    print(lst_robbers['ScientistName'][i], '-', lst_robbers['date'][i])
print('Оригинальный рецепт принадлежит:', lst_robbers['ScientistName'][0])

# запишем готовый новый словарь в новый txt файл
with open('scientist_origin.txt', 'w', encoding='utf8', newline='') as file:
    file.write('ScientistName#preparation#date#components')
    file.write('\n')
    for ind in range(len(new_slovar['ScientistName'])):
        file.write(new_slovar['ScientistName'][ind] + '#' + new_slovar['preparation'][ind] + '#' + new_slovar['date'][ind] + '#' + new_slovar['components'][ind])
        file.write('\n')



