from pymongo import MongoClient
from utils import get_current_time, check_role

import settings

client = MongoClient(settings.MONGO_LINK)
db = client[settings.MONGO_DB] # MONGO_DB - название базы данных

def get_or_create_user(db, update):
    user = db.users.find_one({"user_id" : update.effective_user.id})
    if not user:
        user = {
            "user_id" : update.effective_user.id,
            "first_name" : update.effective_user.first_name,
            "last_name" : update.effective_user.last_name,
            "username" : update.effective_user.username,
            "chat_id" : update.message.chat_id,
            "date" : get_current_time(update.message.date),
            "role" : check_role(update.effective_user.id)
        }
        db.users.insert_one(user)
    return user