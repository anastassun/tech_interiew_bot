import os

def open_file(update, context):
    name_file = ' '.join(context.args)
    basedir = os.path.join('donwloads', name_file)
    doc = {}
    with open(basedir, 'r', encoding='utf-8') as f:
        content = f.read().split("\n")
        print(content)

    for item in content:
        if '•' in item:
            print('Вопрос:', item)
            doc[item] = []
        if '-' in item:
            print('Варианты ответа', item)

    print(doc)
