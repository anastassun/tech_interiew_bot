from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from db import db, info_vacan_in_company, user_profile
from utils import del_use_num, new_button, format_dict, check_phone, main_keyboard
#from format_word_anketa_user import create_word_file

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
        print(context.user_data["vacan"])
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
        context.user_data['question'] = message['blank_form'][context.user_data["slot"]]
        context.user_data['user_id'] = update.effective_user.id
        if user_profile(db, context.user_data['user_id'], context.user_data["slot"]):
            update.message.reply_text("Вы уже собеседовались на эту вакансию")
            return DISCUSSION
        reply_keyboard = [[]]
        reply_keyboard.append(context.user_data['question'])
        update.message.reply_text("Выберите вопрос",
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
            )
        return QUESTION

def quest(update, context):
    num = context.user_data['question']
    old_num = del_use_num(context.user_data)
    new_num = new_button(num, old_num)
    sms = update.message.text
    if sms not in num or sms not in new_num:
        update.message.reply_text("Ошибка. Нажмите доступную кнопку!")
        return QUESTION
    else:
        update.message.reply_text(context.user_data['question'][str(update.message.text)])
        context.user_data['num_answer'] = [str(sms)]
        return NUMQUESTION

def alarm(context):
    context.bot.send_message(chat_id=context.job.context["chat_id"], text="у вас осталось 10 секунд на ответ!")

def num_qestion(update, context):
    num_answer = context.user_data['num_answer']
    context.user_data[num_answer[0]] = update.message.text
    num = context.user_data['question']
    old_num = del_use_num(context.user_data)
    new_buttons = new_button(num, old_num)
    
    
    reply_keyboard = [[]]
    reply_keyboard.append(new_buttons)
    if new_buttons: #Проверяет есть ли еще не нажатые кнопки, если кнопки есть True, если нету False.
        job_context={
        "chat_id":update.message.chat_id,
    }
        context.job_queue.scheduler.remove_all_jobs()
        context.job_queue.run_once(alarm, 10, context=job_context)

        update.message.reply_text('Выберите следующий вопрос',reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
        return QUESTION
    else:
        del context.user_data['num_answer']
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
    try:
        userprofile = format_dict(context.user_data)
        #create_word_file(userprofile)
    except (FileNotFoundError, KeyError, AttributeError, TypeError) as err:
        update.message.reply_text(f'Возникла ошибка {err}', reply_markup=main_keyboard())
        return ConversationHandler.END
    update.message.reply_text('Все ответы записаны', reply_markup=main_keyboard())
    return ConversationHandler.END

def anketa_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")