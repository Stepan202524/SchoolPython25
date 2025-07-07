# Документы
# Word - DOCX (python_docx)
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Inches, Mm, Pt      # Для размеров

doc = Document()        # Создаём экземпляр документа в оперативной памяти
doc.add_heading('Otchet',2) # Добавление заголовка
paragraph = doc.add_paragraph('В этом отчёте есть')     # Создали абзац
paragraph.add_run('ключевые показатели').bold = True     # Добавляем в абзац текс (run - что-то внутри абзаца

paragraph = doc.add_paragraph()     # Новый абзац для списка
paragraph_format = paragraph.paragraph_format
paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
paragraph = doc.add_paragraph('Первый пункт', style='List Bullet')  # Маркированный
paragraph = doc.add_paragraph('Второй пункт', style='List Bullet')
paragraph = doc.add_paragraph('Первый пункт', style='List Number')  # Нумерованный
paragraph = doc.add_paragraph('Второй пункт', style='List Number')
paragraph = doc.add_paragraph()

table = doc.add_table(rows=4, cols=4)       #Добавляем таблицу
for i, row in enumerate(table.rows):        # Заполняем
    for j, cell in enumerate(table.columns):
        cell.text = f'Строка {i + 1}, Столбец {j + 1}'

paragraph = doc.add_paragraph()
doc.add_picture('Kartinka/Spanch.jpg', width=Mm(105))      # Добавляем картинку в doc

doc.save('docs/report.docx')    # Сохраняем в папку