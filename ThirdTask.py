import csv

with open('scientist.txt', encoding='utf8') as f:
    # создадим список словарей с именами, датами и тд
    reader = list(csv.DictReader(f, delimiter='#', quotechar= '"'))

# решение задачи:
input_data = input()
while input_data != 'эксперимент':
    f = 0 # флаг, что нам не встречалась введенная дата
    for el in reader:
        if input_data in el['date']:
            surname, name, sec_name = el['ScientistName'].split()
            prep = el['preparation']
            date = el['date']
            print('Ученый', surname, name[0] + '.' + sec_name[0], 'создал препарат:', prep, '-', date)
            f = 1
    if f == 0:
        print('В этот день ученые отдыхали')
    input_data = input()

