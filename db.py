from pymongo import MongoClient
from utils import check_role
from datetime import datetime

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
            "date" : update.message.date,
            "role" : check_role(update.effective_user.id)
        }
        db.users.insert_one(user)
    return user

def save_anketa(db, anketa_data):
    user = db.users.find_one({"user_id" : anketa_data['user_id']})
    anketa_data['time'] = datetime.now()
    del anketa_data['user_id']
    if not 'anketa' in user:
        db.users.update_one({'_id': user['_id']}, {'$set': {'anketa': [anketa_data]}})
    else:
        db.users.update_one({'_id': user['_id']}, {'$push': {'anketa': anketa_data}})

def get_or_create_job(db, file):
    job = db.jobs.find_one({'secret_key' : file['secret_key']})
    if not job:
        job = {
            'secret_key' : file['secret_key'],
            'vacancy' : file['vacancy'],
            'company' : file['company'],
            'blank_form' : file['blank_form']
            }
        db.jobs.insert_one(job)
    return job

def info_vacan_in_company(db, vacan):
    job = db.jobs.find_one({'vacancy' : vacan})
    return job

def user_name_and_phone(db, user_id):
    user = db.users.find_one({'user_id': user_id})
    if not user['anketa'][0]['phone']:
        return False
    return user

def user_profile(db, user_id, slot):
    if db.users.find_one({'user_id': user_id, 'anketa.slot': slot}):
        return True
    return False