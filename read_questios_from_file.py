doc_android = {}
with open('Скрининг_Android.txt', 'r', encoding='utf-8') as f:
    content = f.read().split("\n")
    #print(content)

for item in content:
    if '•' in item:
        print('Вопрос:', item)
        #doc[item] = [1,2,3,4]
    if '-' in item:
        print('', item)

print(doc_android)
