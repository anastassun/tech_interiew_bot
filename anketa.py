from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from db import db, info_vacan_in_company, save_anketa, get_or_create_user
from utils import get_key, del_use_num, new_button, format_dict

NAME, DISCUSSION, QUESTION, NUMQUESTION, CONTACT, FINAL = range(6)

def start (update, context):
    update.message.reply_text (
        'Привет, как вас зовут?',
    reply_markup=ReplyKeyboardRemove()
    ) 
    context.user_data["vacan"] = update.message.text
    return NAME

def name(update,context):
    user_name = update.message.text
    user = get_or_create_user(db, update)
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста введите имя и фамилию")
        return NAME
    else:
        message = info_vacan_in_company(db, context.user_data["vacan"])
        context.user_data["name"] = user_name
        if len(message) > 1:
            reply_keyboard = [[]]
            reply_keyboard.append(message['blank_form'])
            update.message.reply_text(
                "Выберите направление",
                reply_markup=ReplyKeyboardMarkup(reply_keyboard)
            )
            return DISCUSSION
        else:
            reply_keyboard = [[]]
            for num in range(1,len(message)+1):
                reply_keyboard.append(f"Вопрос: №{message['blank_form']}")
            update.message.reply_text(
                "Выберите вопрос",
                reply_markup=ReplyKeyboardMarkup(reply_keyboard)
            )
            return DISCUSSION

def discussion(update, context):
    message = info_vacan_in_company(db, context.user_data["vacan"])
    if update.message.text not in message['blank_form']:
        update.message.reply_text("Ошибка. Нажмите доступную кнопку!")
        return DISCUSSION
    else:
        context.user_data["slot"] = update.message.text
        reply_keyboard = [[]]
        reply_keyboard.append(message['blank_form'][context.user_data["slot"]])
        update.message.reply_text("Выберите вопрос",
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
            )
        return QUESTION

def quest(update, context):
    message = info_vacan_in_company(db, context.user_data["vacan"])
    if update.message.text not in message['blank_form'][context.user_data["slot"]]:
        update.message.reply_text("Ошибка. Нажмите доступную кнопку!")
        return QUESTION
    else:
        update.message.reply_text(message['blank_form'][context.user_data["slot"]][str(update.message.text)])
        context.user_data[update.message.text] = 'proverka'
    return NUMQUESTION

def num_qestion(update, context):
    message = info_vacan_in_company(db, context.user_data["vacan"])
    if len(message['blank_form'][context.user_data["slot"]])+3 != len(context.user_data):
        context.user_data['proverka'] = update.message.text
        dicts = context.user_data
        dicts = get_key(dicts)
        num = message['blank_form'][context.user_data["slot"]]
        old_num = del_use_num(dicts)
        new_buttons = new_button(num, old_num)
        reply_keyboard = [[]]
        reply_keyboard.append(new_buttons)
        update.message.reply_text('Следующий вопрос',reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
        return QUESTION
    else:
        context.user_data['proverka'] = update.message.text
        dicts = context.user_data
        dicts = get_key(dicts)
        num = message['blank_form'][context.user_data["slot"]]
        old_num = del_use_num(dicts)
        new_buttons = new_button(num, old_num)
        reply_keyboard = [[]]
        reply_keyboard.append(new_buttons)
        update.message.reply_text('Конец, скажите мне пока.',reply_markup=ReplyKeyboardRemove(reply_keyboard, resize_keyboard=True))
        return FINAL

def final(update, context): 
    update.message.reply_text('Все ответы записаны')
    done = format_dict(context.user_data)
    save_anketa(db,update.effective_user.id, done)
    return ConversationHandler.END

def anketa_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")