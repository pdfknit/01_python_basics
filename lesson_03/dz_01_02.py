# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык

def num_translate_adv(word):
    dictionary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    title = True if word.istitle() else False
    word = word.lower()
    translated_word = dictionary[word] if word in dictionary.keys() else None
    return translated_word.title() if title else translated_word


word = input('Введите число на английском или «Enter» для выхода из программы:\n')
while word != '':
    print(num_translate_adv(word))
    word = input('Введите число на английском:\n')
