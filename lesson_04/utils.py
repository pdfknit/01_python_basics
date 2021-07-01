from requests import get
import datetime


def currency_rates(argv):
    program, *args = argv
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    all_courses = response.content.decode(encoding=response.encoding)
    for money_code in args:
        course_to_rub = None
        money_code = money_code.upper()
        for recent_valute in all_courses.split('<Valute ID=')[1:]:
            if money_code in recent_valute:
                course_to_rub = float(recent_valute.split('<Value>')[1].strip('</Value></Valute>').replace(',', '.'))
        date_list = all_courses.split('Date="')[1].split('"')[0].split('.')
        today = datetime.date(year=int(date_list[2]), month=int(date_list[1]), day=int(date_list[0]))
        print(f'{money_code} to RUB:', course_to_rub, today)


if __name__ == '__main__':
    import sys

    currency_rates(sys.argv)
