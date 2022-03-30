from logging.handlers import RotatingFileHandler
#from unicodedata import name
from telegram import ReplyKeyboardRemove, ParseMode , InlineKeyboardButton, InlineKeyboardMarkup ,ReplyKeyboardMarkup
from telegram.ext import ConversationHandler 



def anketa_start (update, context):
    update.message.reply_text (
        'Привет, как вас зовут?',
    reply_markup=ReplyKeyboardRemove()
    ) 
    return "name" 

def question1(update,context): 
    context.user_data["answer1"] = update.message.text
    update.message.reply_text(
        "Что ищешь на новом месте работы? Что важно, приоритетно?"
    )
    return "question2"
  

def question2(update,context): 
    context.user_data["answer2"] = update.message.text
    update.message.reply_text(
        "Почему рассматриваешь предложения?"
    )
    return "question3"  

def question3(update,context): 
    context.user_data["answer3"] = update.message.text
    update.message.reply_text(
        "Когда готов выйти на новую работу?"
    )
    return "question4"

def question4(update,context): 
    context.user_data["answer4"] = update.message.text
    update.message.reply_text(
        "Какие пожелания к формату работы (полная удаленка или другой город (не Москва) и название города)?"
    )
    return "question5"  

def question5(update,context): 
    context.user_data["answer5"] = update.message.text
    update.message.reply_text(
        "К какому уровню себя относишь (jun-senior)?(Для лидов: как долго занимаешься руководством и какова численность в подчинении? Используете скрам, канбан или просто, как продуктовую команду? Хочешь в менеджерскую позицию – тимлид или техлид/архитектор)?"
    )
    return "question6"  

def question6(update,context): 
    context.user_data["answer6"] = update.message.text
    update.message.reply_text(
        "Что нравится в работе/задачах/коллективе? Что получается делать лучше всего?"
    )
    return "question7"

def question7(update,context): 
    context.user_data["answer7"] = update.message.text
    update.message.reply_text(
        "Что не нравится в работе/задачах/коллективе? Что не нравится или не получается делать в профессии?"
    )
    return "rating" 

def anketa_name(update,context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста введите имя и фамилию")
        return "name"
    else:
        context.user_data["anketa"] ={"name": user_name}
        update.message.reply_text(
            "Перейдите к первому вопросу. Для этого нажмите /next")
        #reply_markup=ReplyKeyboardMarkup(one_time_keyboard=True))
        
        return  "question1"

def anketa_rating(update,context): 
    context.user_data ["anketa"]["rating"] = update.message.text
    update.message.reply_text(
        "Оставьте комментарий в свободной форме или пропустите этот шаг, введя /skip"
    )
    return "comment"

def anketa_comment(update, context):
    context.user_data["anketa"]["comment"] = update.message.text
    user_text = f"""<b>Имя Фамилия:</b> {context.user_data['anketa']['name']}
<b>Вопрос 1:</b> {context.user_data['answer1']}
<b>Вопрос 2:</b> {context.user_data['answer2']}
<b>Вопрос 3:</b> {context.user_data['answer3']}
<b>Вопрос 4:</b> {context.user_data['answer4']}
<b>Вопрос 5:</b> {context.user_data['answer5']}
<b>Вопрос 6:</b> {context.user_data['answer6']}
<b>Вопрос 7:</b> {context.user_data["anketa"]["rating"]}
<b>Комментарий:</b> {context.user_data['anketa']['comment']}"""

    update.message.reply_text(user_text,parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def anketa_skip(update, context):
    user_text = f"""<b>Имя Фамилия:</b> {context.user_data['anketa']['name']}
<b>Оценка:</b> {context.user_data['anketa']['rating']}"""

    update.message.reply_text(user_text,parse_mode=ParseMode.HTML)
    return ConversationHandler.END

#def help(bot,update):
        #keyboard = [
           # [InlineKeyboardButton(u"HELP", callback_data=str("HELP"))]
        #]
        #reply_markup = InlineKeyboardMarkup(keyboard)
        #update.message.reply_text(
            #"Help handler, Press button",
            #reply_markup=reply_markup
        #)

        #return "HELP"

def anketa_dontknow(update, context):
    update.message.reply_text("Не понимаю")


