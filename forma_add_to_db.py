import db as db_add

def add_quest_vacan_slot(info, vacan):
    format_add_db_dict = create_dict_db(info, vacan)
    db_add.get_or_create_job(db_add.db, format_add_db_dict)
    return 'Данные успешно добавлены'

def create_dict_db(blank, vacancy):
    db_dict = {'vacancy': vacancy, 'blank_form': blank}
    return db_dict