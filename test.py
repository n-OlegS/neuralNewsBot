import json


with open('/Users/oleg/Downloads/Telegram Desktop/ChatExport_2022-04-27/result.json') as file:
    d = json.load(file)
    file.close()
    # print(d)

#print(new_new_words)
words = []
for elem in list(d["messages"]):
    if "text" in list(elem.keys()):
        #print(elem)
        if isinstance(elem["text"], str):
            if elem["text"]:
                words.append(elem["text"])




words = list(map(lambda x: x.replace('\n', ''), words))
new_words = []
for elem in words:
    for i in elem.split():
        if i:
            j = -1
            while j < len(i) - 1:
                j += 1
                if not i[j].isalpha() and i[j] != ".":
                    i = i.replace(i[j], "")
            if '.' not in i:
                new_words.append(i.lower())
            else:
                if i.find('.') == len(i) - 1:
                    new_words.append(i.lower().replace('.', ''))
                    new_words.append('.')

words = new_words.copy()
d = {}
'''
for i in range(len(words)):
    w = new_words[i]
    lw = new_words[i-1]
    if lw.isalpha():
        if lw in list(d.keys()):
            d[lw].append(w)
        else:
            d[lw] = [str(new_words[i])]
 '''

for i in range(1, len(words)):
    w = words[i]
    lw = words[i - 1]
    if lw.isalpha():
        if lw in list(d.keys()):
            d[lw].append(w)
        else:
            d[lw] = [str(new_words[i])]

print(d)