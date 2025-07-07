# Документы (электронные таблицы)
# Excel (openpyxl)
from openpyxl import Workbook
wb = Workbook()     # Создание таблицы в конструкторе (Пустой excel файл)
ws = wb.active
ws.title = 'Otchet'
wb.save = ('docs/report.xlsx')

from openpyxl import load_workbook
wb = load_workbook('docs/report.xlsx')  # Открываем(загружаем) рабочую книгу
ws = wb.active                          # Активный лист
ws['A1'] = 'FIO'                        # Заголовки
ws['B1'] = 'Doljnost'
ws['C1'] = 'Otdel'
employees = [                           # данные
    ['Иванов', 'Дирик', 'Firma'],
    ['Petrov', 'Buhgalter', 'Financy'],
    ['Sydorov', 'Analitik', 'IT'],
]
for row, data in enumerate(employees, start=2):
    ws.cell(row=row, column=1, value=data[0])
    ws.cell(row=row, column=2, value=data[1])
    ws.cell(row=row, column=3, value=data[2])

ws['F1'] = 'Privet 555'                 # Способы записи
# ws.cell(row=1, column=3, value='Hello')
wb.save('docs/newtable.xlsx')

wb = load_workbook('docs/newtable.xlsx')            # Чтение данных
ws = wb.active
rows_count = ws.max_row     # Число заполненных строк
for row in ws.iter_rows(values_only=True):
    fio, pos, dept = row
    print(f'Familia: {fio}, Doljnost: {pos}, Otdel: {dept}')

# Работа с формулами
# ws['A1'] = "=SUM(A1:A10)"
