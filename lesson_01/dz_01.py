# TODO: Реализовать вывод информации в промежутке времени в зависимости от его продлжительности

duration = int(input('Введите продолжительность (ноль для выхода):\n'))

while duration > 0:

    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    secs = (duration % 3600) % 60

    if days > 0:
        print(days, 'дн', hours, 'час', minutes, 'мин', secs, 'сек')
    elif hours > 0:
        print(hours, 'час', minutes, 'мин', secs, 'сек')
    elif minutes > 0:
        print(minutes, 'мин', secs, 'сек')
    else:
        print(secs, 'сек')

    duration = int(input('Введите продолжительность:\n'))
