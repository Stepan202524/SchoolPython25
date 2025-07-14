# CSV-файлы
import csv
# with open('people.csv', 'r', encoding='utf-8') as f:
#     dict_reader = csv.DictReader(f)
#     for row in dict_reader:
#         print(f'{row['name']} jivet v gorode {row['city']}')

# field_names = ['name', 'age', 'city']       # Имена полей
# data = {
#     'name' : 'Boris',
#     'age' : 22,
#     'city' : 'MSk'
# }
# with open('file.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=field_names)
#     writer.writerow(data)

# Режимы квотирования
data1 = ['name', 35, 'town']
with open('sample.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(data1)

# data = [
#     ['name', 'age', 'city'],
#     ['Женя', '46', 'Клн'],
#     ['Рома', '18', 'СПб'],
#     ['Павел', '35', 'Мск']
# ]
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',', quotechar='"')
#     for row in reader:
#         print(row)
#
# with open('emloyee.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)