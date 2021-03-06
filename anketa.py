import logging

from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from db import db, info_vacan_in_company, user_name_and_phone, user_profile
from utils import del_use_num, new_button, format_dict, check_phone, main_keyboard, inline_keyboard, vac_keyboard
from format_word_anketa_user import create_word_file

NAME, DISCUSSION, QUESTION, NUMQUESTION, CONTACT, FINAL = range(6)

def start (update, context):
    context.user_data["vacan"] = update.message.text
    context.user_data['info_vacan'] = info_vacan_in_company(db, context.user_data["vacan"])
    user = user_name_and_phone(db, update.effective_user.id)
    if user == False:
        update.message.reply_text (
            f'Привет, как вас зовут?',
        reply_markup=ReplyKeyboardRemove())
        return NAME
    else:
        context.user_data['old_info'] = user['anketa'][0]
        context.user_data['name'] = context.user_data['old_info']['name']
        reply_keyboard = vac_keyboard(context.user_data['info_vacan']['blank_form'])
        update.message.reply_text(
            f"Я вас узнал, давайте продолжим, выберите направление.",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard))
        return DISCUSSION

def yes(update, context):
    update.callback_query.edit_message_text(text=f"Продолжим?")
    if not 'phone' in context.user_data:
        context.user_data['phone'] = context.user_data['old_info']['phone']
        return FINAL

def no(update, context):
    update.callback_query.edit_message_text(text=f"Скажите новые данные")
    if not 'phone' in context.user_data:
        return CONTACT

def name(update,context):
    user_name = update.message.text
    reply_keyboard = vac_keyboard(context.user_data['info_vacan']['blank_form'])
    if len(user_name.split()) < 2 and not 'name' in context.user_data:
        update.message.reply_text("Пожалуйста введите имя и фамилию")
        return NAME
    else:
        context.user_data["name"] = user_name
        update.message.reply_text(
            "Выберите направление",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard)
        )
        return DISCUSSION

def discussion(update, context):
    if update.message.text not in context.user_data['info_vacan']['blank_form']:
        update.message.reply_text("Ошибка. Нажмите доступную кнопку!")
        return DISCUSSION
    else:
        context.user_data["slot"] = update.message.text
        context.user_data['question'] = context.user_data['info_vacan']['blank_form'][context.user_data["slot"]]
        context.user_data['user_id'] = update.effective_user.id
        if user_profile(db,update.effective_user.id,context.user_data["slot"]):
            update.message.reply_text("Вы уже собеседовались на эту вакансию")
            return DISCUSSION
        reply_keyboard = [[]]
        reply_keyboard.append(context.user_data['question'])
        update.message.reply_text("Выберите вопрос",
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
            )
        return QUESTION

def quest(update, context):
    num = context.user_data['question']
    old_num = del_use_num(context.user_data)
    new_num = new_button(num, old_num)
    up_mes_text = update.message.text
    if up_mes_text not in num or up_mes_text not in new_num:
        update.message.reply_text("Ошибка. Нажмите доступную кнопку!")
        return QUESTION
    else:
        update.message.reply_text(context.user_data['question'][str(up_mes_text)])
        context.user_data['num_answer'] = [str(up_mes_text)]
        return NUMQUESTION

def num_qestion(update, context):
    num_answer = context.user_data['num_answer']
    context.user_data[num_answer[0]] = update.message.text
    old_num = del_use_num(context.user_data)
    new_buttons = new_button(context.user_data['question'], old_num)
    reply_keyboard = [[]]
    reply_keyboard.append(new_buttons)
    #Проверяет есть ли еще не нажатые кнопки, если кнопки есть True, если нету False.
    if new_buttons:
        update.message.reply_text('Выберите следующий вопрос',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
        return QUESTION
    else:
        del context.user_data['num_answer']
        if 'old_info' in context.user_data:
            update.message.reply_text(f"Ваш телефон: {context.user_data['old_info']['phone']}", 
            reply_markup=inline_keyboard())
            return CONTACT
        update.message.reply_text('Скажите свой номер телефона',
        reply_markup=ReplyKeyboardRemove(reply_keyboard, resize_keyboard=True))
        return CONTACT

def contact(update, context):
    user_phone = update.message.text
    check = check_phone(user_phone)
    if not check:
        update.message.reply_text("Неправильно набран номер",
        reply_markup=ReplyKeyboardRemove())
        return CONTACT
    else:
        context.user_data['phone'] = update.message.text
        update.message.reply_text(f"Место для комментария или отзыва.", 
                                    reply_markup=ReplyKeyboardRemove())
        return FINAL

def final(update, context): 
    try:
        userprofile = format_dict(context.user_data)
        create_word_file(userprofile)
    except (FileNotFoundError, KeyError, AttributeError, TypeError) as err:
        update.message.reply_text(f'Возникла ошибка', reply_markup=main_keyboard())
        logging.error(f'KeyError {err} from db')
        return ConversationHandler.END
    update.message.reply_text('Все ответы записаны', reply_markup=main_keyboard())
    return ConversationHandler.END

def anketa_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")