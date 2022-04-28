import json


with open(input()) as file:
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
            i = i.replace(",", "").replace(":", '').replace(";", '').replace("-", '').replace("«", '').replace("»", '')
            if '.' not in i:
                new_words.append(i.lower())
            else:
                if i.find('.') == len(i) - 1:
                    new_words.append(i.lower().replace('.', ''))
                    new_words.append('.')

words = new_words.copy()
d = {}

for i in range(1, len(words)):
    w = words[i]
    lw = words[i - 1]
    if lw.isalpha():
        if lw in list(d.keys()):
            d[lw].append(w)
        else:
            d[lw] = [str(new_words[i])]

with open('/Users/oleg/PycharmProjects/neuralNews/d.json', 'w') as file:
    json_string = json.dumps(d, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    file.write(json_string)

#print(d)