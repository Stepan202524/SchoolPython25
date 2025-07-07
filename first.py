# Документы
# Word - DOCX (python_docx)
# DOCX (docxtpl)
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Inches, Mm, Pt      # Для размеров
from docxtpl import DocxTemplate

doc = DocxTemplate('docs/template.docx')    #Загрузка шаблона
content = {
    'company': 'Монолит',
    'employee': 'Петров Г. Ю.',
    'position': 'Дирик',
    'date': '15/08/2022'
}
doc.render(content)     # Добавляем словарь с переменными в документ
doc.save('docs/about.docx')