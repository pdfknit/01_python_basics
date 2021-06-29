# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык

def num_translate_adv(word):
    dictionary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    title = word.istitle()
    word = word.lower()
    translated_word = dictionary.get(word)
    if translated_word != None:
        translated_word = translated_word.title() if title else translated_word
    return translated_word


word = input('Введите число на английском или «Enter» для выхода из программы:\n')
while word != '':
    print(num_translate_adv(word))
    word = input('Введите число на английском:\n')