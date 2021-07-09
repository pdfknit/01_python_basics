tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

result = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(0, len(tutors)))

for _ in range(0, len(tutors)):
    print(next(result))
    print(type(result))
