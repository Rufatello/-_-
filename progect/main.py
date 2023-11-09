import openpyxl
import os
for root, dirs, files in os.walk('/home/geydarovr/Загрузки/errors_employees/progect'):
    for file in files:
        if file.endswith('.xlsx'):
            os.rename(file, 'ошибки сотрудников.xlsx')

wb = openpyxl.load_workbook('ошибки сотрудников.xlsx')
sheets = wb.active
for i in range(2, sheets.max_row+1):
    b = sheets[i][9].value
    if b =='Неверный АРМ':
        sheets.cell(row=i, column=11).value = 'зайти под верным АРМ и переподписать'
    elif b=='СНИЛС':
        sheets.cell(row=i, column=11).value = 'Запросить СНИЛС пациента'
    elif b=='На дату создания документа для указанного вида требуется как минимум 1 подпись роли [DOCTOR]':
        sheets.cell(row=i, column=11).value = 'При подписании выбрать правильную роль: Врач'
    else:
        sheets.cell(row=i, column=11).value = 'Тут ничего не нужно'

wb.save('ошибки сотрудников.xlsx')