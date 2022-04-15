import os
import logging
from docx import Document
from forma_add_to_db import add_quest_vacan_slot

def open_file_txt(name_file, name_vacan):
    basedir = os.path.join('donwloads', name_file)
    with open(basedir, 'r', encoding='utf-8') as f:
        content = f.read().split("\n")
    dict_quest = dict()
    for item in content:
        if '*' in item:
            vac = item.replace("*",'')
            num = 1
            vacan = dict()
        else:
            vacan[str(num)] = item
            num += 1
        dict_quest[vac] = vacan
    text_msg = add_quest_vacan_slot(dict_quest, name_vacan)
    return text_msg

def open_file_docx(name_file, name_vacan):
    basedir = os.path.join('donwloads', name_file)
    doc = Document(basedir)
    dict_quest = dict()
    try:
        for paragraph in doc.paragraphs:
            if paragraph.text:
                if '*' in paragraph.text:
                    vac = paragraph.text.replace("*",'')
                    num = 1
                    vacan = dict()
                else:
                    vacan[str(num)] = paragraph.text
                    num += 1
                dict_quest[vac] = vacan
        text_msg = add_quest_vacan_slot(dict_quest, name_vacan)
    except UnboundLocalError as err:
        text_msg = 'Вы забыли поставить метку около вакансии "*"'
        logging.error(f'Ошибка {err} | from open_console_file')
    return text_msg