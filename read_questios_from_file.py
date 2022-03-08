doc = {}
with open('Скрининг_Android.txt', 'r', encoding='utf-8') as f:
    content = f.read().split("\n")
    #print(content)

for item in content:
    if '•' in item:
        #print('Вопрос:', item)
        doc[item] = []
    # if '-' in item:
        #print('Варианты ответа', item)

print(doc)
