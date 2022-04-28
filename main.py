import random, json
global final

with open('/Users/oleg/PycharmProjects/neuralNews/d.json') as file:
    d = json.load(file)
    file.close()

orig = input()
final = orig

def gen_word(word):
    global final

    new_word = random.choice(d[word])

    if new_word == '.':
        final += '.'
        return
    else:
        final += ' ' + new_word
        gen_word(new_word)

gen_word(final)

while not 3 < len(final.split()) < 12:
    final = orig
    gen_word(final)

print(final.capitalize())
