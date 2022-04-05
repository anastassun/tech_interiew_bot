from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from db import db, info_vacan_in_company, save_anketa
from utils import del_use_num, new_button, format_dict, check_phone, main_keyboard
from format_word_anketa_user import create_word_file

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
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста введите имя и фамилию")
        return NAME
    else:
        message = info_vacan_in_company(db, context.user_data["vacan"])
        context.user_data["name"] = user_name
        reply_keyboard = [[]]
        reply_keyboard.append(message['blank_form'])
        update.message.reply_text(
            "Выберите направление",
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
    num = message['blank_form'][context.user_data["slot"]]
    old_num = del_use_num(context.user_data)
    new_num = new_button(num, old_num)
    sms = update.message.text
    if sms not in num or sms not in new_num:
        update.message.reply_text("Ошибка. Нажмите доступную кнопку!")
        return QUESTION
    else:
        update.message.reply_text(message['blank_form'][context.user_data["slot"]][str(update.message.text)])
        context.user_data['num_answer'] = [str(sms)]
        return NUMQUESTION

def num_qestion(update, context):
    message = info_vacan_in_company(db, context.user_data["vacan"])
    num_answer = context.user_data['num_answer']
    context.user_data[num_answer[0]] = update.message.text
    del context.user_data['num_answer']
    dicts = context.user_data
    num = message['blank_form'][context.user_data["slot"]]
    old_num = del_use_num(dicts)
    new_buttons = new_button(num, old_num)
    reply_keyboard = [[]]
    reply_keyboard.append(new_buttons)

    if len(message['blank_form'][context.user_data["slot"]])+3 != len(context.user_data):
        update.message.reply_text('Выберите следующий вопрос',reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
        return QUESTION
    else:
        update.message.reply_text('Скажите свой номер телефона',reply_markup=ReplyKeyboardRemove(reply_keyboard, resize_keyboard=True))
        return CONTACT

def contact(update, context):
    user_phone = update.message.text
    check = check_phone(user_phone)
    if not check:
        update.message.reply_text("Неправильно набран номер")
        return CONTACT
    else:
        context.user_data['phone'] = update.message.text
        update.message.reply_text("Место для комментария или отзыва.")
        return FINAL

def final(update, context): 
    update.message.reply_text('Все ответы записаны', reply_markup=main_keyboard())
    done = format_dict(context.user_data)
    save_anketa(db,update.effective_user.id, done)
    create_word_file(done)
    return ConversationHandler.END

def anketa_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")