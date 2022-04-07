from telegram import ReplyKeyboardMarkup
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
        ]
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
    good_dict = {'user_id': dicts['user_id'], 'vacan': dicts['vacan'], 'name' : dicts['name'],'phone': dicts['phone'], 'slot': dicts['slot'], 'answer': dict(answer), 'question': dicts['question']}
    return good_dict

def check_phone(phone):
    format_phone = re.sub(r'\b\D', '', phone)
    clear_phone = re.sub(r'[\ \(]?', '', format_phone)
    if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$',phone):
        return (bool(phone))
    else: 
        return False 

