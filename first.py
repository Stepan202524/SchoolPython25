# Zip
from zipfile import ZipFile
import os
# Архивируем все файлы .csv в Zip
# csv_files = [f for f in os.listdir() if f.endswith('.csv')]
# print(csv_files)
# with ZipFile('archiv.zip', 'w') as myzip:
#     for file in csv_files:
#         myzip.write(file)
#         os.remove(file)

# Извлечение файлов из архива
files_to_exctract = ['people.csv', 'file.csv']
with ZipFile('archiv.zip', 'r') as zip_obj:
    zip_obj.extractall(members=files_to_exctract)
# Получить список файлов в архиве
with ZipFile('archiv.zip', 'r') as zip_obj:
    print(zip_obj.namelist())