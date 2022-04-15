from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from open_console_file import open_file_txt, open_file_docx
import constants
import settings
import re

def info_bot():
    with open('bot_info.txt', 'r', encoding='utf8') as f:
        return f.read()

def main_keyboard():
    return ReplyKeyboardMarkup([
        ["Информация о боте",  
        "Начать беседу"]
        ])

def vacansies_keyboard():
    return ReplyKeyboardMarkup(
        [ 
        ["Java Developer"], 
        ["Java 2 Developer"] , 
        ["Android Develope"],
        ['QA Automation'],
        ["IOS developer"],
        ["SQL Developer"]
        ], one_time_keyboard=True
    )

def check_role(user_id):
    if user_id in settings.ADMIN:
        return constants.ADMIN
    return constants.USER

def del_use_num(dicts):
    num = []
    for key in dicts:
        if key.isdigit():
            num.append(key)
        else:
            continue
    return num

def new_button(num, use_num):
    new_num = []
    all_num = [an for an in num]
    for n in all_num:
        if n not in use_num:
            new_num.append(n)
    return new_num

def format_dict(dicts):
    answer = dict()
    for key in dicts:
        if key.isdigit():
            answer[key] = dicts[key]
    good_dict = {'user_id': dicts['user_id'], 'vacan': dicts['vacan'], 
                'name' : dicts['name'],'phone': dicts['phone'], 'slot': dicts['slot'], 
                'answer': dict(answer), 'question': dicts['question']}
    return good_dict

def check_phone(phone):
    format_phone = re.sub(r'\b\D', '', phone)
    clear_phone = re.sub(r'[\ \(]?', '', format_phone)
    if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$',phone):
        return (bool(phone))
    else: 
        return False 

def inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('ДА', callback_data='ДА'),
            InlineKeyboardButton('НЕТ', callback_data='НЕТ'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def info_format_file(name_file):
    format_file = (name_file.split('.')[-1])
    name_vacan = (name_file.split('.')[0])
    if format_file == 'txt':
        text_msg = open_file_txt(name_file, name_vacan)
    if format_file == 'docx':
        text_msg = open_file_docx(name_file, name_vacan)  
    else:
        text_msg = 'Данные не загружены в базу'
    return text_msg

def vac_keyboard(vac_list):
    keyboard = [[]]
    keyboard.append(vac_list)
    return keyboard

