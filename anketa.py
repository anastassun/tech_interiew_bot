from logging.handlers import RotatingFileHandler
from unicodedata import name
from telegram import ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler


def anketa_start (update, context):
    update.message.reply_text (
        'Привет, как вас зовут?',
    reply_markup=ReplyKeyboardRemove()
    ) 
    return "name" 
    
def anketa_name(update,context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста введите имя и фамилию")
        return "name"
    else:
        context.user_data["anketa"] ={"name": user_name}
        reply_keyboard =[{"1","2","3","4"}]
        update.message.reply_text(
            "Пожалуйста оцените нашего бота от 1 до 4",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return rating

def anketa_rating(update,context): 
    context.user_data["anketa"]["rating"] = int(update.message.text)

    update.message.reply_text(
        "Оставьте комментарий в свободной форме или пропустите этот шаг, введя /skip"
    )
    return "comment"

def anketa_comment(update, context):
    context.user_data["anketa"]["comment"] = update.message.text
    user_text = f"""<b>Имя Фамилия:</b> {context.user_data['anketa']['name']}
<b>Оценка:</b> {context.user_data['anketa']['rating']}
<b>Комментарий:</b> {context.user_data['anketa']['comment']}"""

    update.message.reply_text(user_text,parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def anketa_skip(update, context):
    user_text = f"""<b>Имя Фамилия:</b> {context.user_data['anketa']['name']}
<b>Оценка:</b> {context.user_data['anketa']['rating']}"""

    update.message.reply_text(user_text,parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def anketa_dontknow(update, context):
    update.message.reply_text("Не понимаю")
