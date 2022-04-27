from test import d
import random

global final
final = ''
words = {}


def gen_word(word):
    new_word = random.choice(d[word])
    if new_word == '.':
        final += '.'
        return
    else:
        final += ' ' + new_word
        gen_word(new_word)


gen_word(input())
print(final)
