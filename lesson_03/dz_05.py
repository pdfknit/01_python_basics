import random


def get_jokes(count_of_jokes, repeat):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    max_repeat = max(len(nouns), len(adverbs), len(adjectives))

    if not repeat and (int(count_of_jokes) > max_repeat):
        jokes_list = 'Не могу сделать столько шуток без повтора слов. Максимальное количество: 5'
    else:
        if repeat:
            for jokes in range(0, int(count_of_jokes)):
                jokes_list.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')

        else:
            for items in range(0, int(count_of_jokes)):
                cur_noun = random.choice(nouns)
                cur_adverb = random.choice(adverbs)
                cur_adjective = random.choice(adjectives)
                jokes_list.append(f'{cur_noun} {cur_adverb} {cur_adjective}')
                nouns.remove(cur_noun)
                adverbs.remove(cur_adverb)
                adjectives.remove(cur_adjective)
    return jokes_list


count_of_jokes = input('Сколько шуток пошутить?\n')
repeat = False if input('Можно повторять слова (+/-)?\n') == '-' else True

print(get_jokes(count_of_jokes, repeat))
