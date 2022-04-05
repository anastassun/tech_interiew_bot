from docx import Document
from docx.shared import Pt
from db import db, info_vacan_in_company
import os

def create_word_file(done):
    os.makedirs('userfile', exist_ok=True)
    a = done['name'].strip()
    b = (done['slot'].replace('/', '_')).strip()
    name_file = f"{a}-{b}.docx"
    basedir = os.path.join('userfile', name_file)
    info_quest = info_vacan_in_company(db, done['vacan'])
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
    doc.add_heading('Информация о человеке', 1)
    name = doc.add_paragraph("Имя и фамилия: ")
    name.add_run(done['name'])
    phone = doc.add_paragraph("Номер телефона: ")
    phone.add_run(done['phone'])
    vacan = doc.add_paragraph("Вакансия: ")
    vacan.add_run(done['vacan'])
    slot = doc.add_paragraph("Должность: ")
    slot.add_run(done['slot'])
    doc.add_heading('Результаты опроса', 1)
    for num in range(1, len(done['answer'])+1):
        doc.add_paragraph(f"Вопрос {num}:\n{info_quest['blank_form'][done['slot']][str(num)]}")
        doc.add_paragraph(f"Ответ {num}:\n{done['answer'][str(num)]}")
    doc.save(basedir)