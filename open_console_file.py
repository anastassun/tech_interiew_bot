import os

def open_file(name_file):
    #print(name_file)
    basedir = os.path.join('donwloads', name_file)
    doc = {}
    with open(basedir, 'r', encoding='utf-8') as f:
        content = f.read().split("\n")
        #print(content)
    dict_quest = dict()
    for item in content:
        if '*' in item:
            vac = item.replace("*",'')
            num = 1
            vacan = dict()
        else:
            vacan[str(num)] = item
            num += 1
        dict_quest[vac] = vacan
    return dict_quest
