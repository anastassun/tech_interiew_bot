from turtle import goto
from telegram import ReplyKeyboardMarkup
import constants
import settings

def info_bot():
    with open('bot_info.txt', 'r', encoding='utf8') as f:
        return f.read()

def main_keyboard():
    return ReplyKeyboardMarkup([
        ["Информация о боте",  
        "Начать тест"]
        ])

def vacansies_keyboard():
    return ReplyKeyboardMarkup(
        [ 
        ["Java Developer"], 
        ["Java 2 Developer"] , 
        ["Android Develope"],
        ['QA Automatio'],
        ["IOS developer"],
        ["SQL Developer"]
        ]
    )

def check_role(user_id):
    if user_id in settings.ADMIN:
        return constants.ADMIN
    return constants.USER

def get_key(dicts):
    for key, value in dicts.items():
        if value == 'proverka':
            a = key
        if key == 'proverka':
            b = value
    dicts[a] = b
    del dicts['proverka']
    return dicts

def del_use_num(dicts):
    num = []
    for key in dicts:
        if key.isdigit():
            key = int(key)
            num.append(key)
        else:
            continue
    return num

def new_button(num, use_num):
    new_num = []
    all_num = [an for an in num]
    old_num = [str(n) for n in use_num]
    for n in all_num:
        if n not in old_num:
            new_num.append(n)
    return new_num

def format_dict(dicts):
    answer = dict()
    for key in dicts:
        if key.isdigit():
            answer[key] = dicts[key]
    good_dict = {'vacan': dicts['vacan'], 'name' : dicts['name'], 'slot': dicts['slot'], 'answer': dict(answer)}
    return good_dict

