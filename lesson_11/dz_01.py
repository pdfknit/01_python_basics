class Date:
    @classmethod
    def to_type_int(cls, date):
        date_list = cls._validator(date)
        return date_list

    @staticmethod
    def _validator(date):
        try:
            date_list = [int(dat) for dat in date.split('-')]
            if date_list[0] <= 31 and date_list[0] > 0:
                if date_list[1] <= 12 and date_list[1] > 0:
                    if date_list[2] in range(1800, 9999):
                        return date_list
            raise ValueError('Wrong date format, "day-month-year", year from 1800 to 9999')
        except:
            raise ValueError('Wrong date format')


date_01 = Date()
date_02 = Date()
date_03 = Date()
date_04 = Date()
date_05 = Date()

print(date_01.to_type_int('12-06-1990'))
# print(date_02.to_type_int('3-12-1888'))
# print(date_04.to_type_int('3-30-1990'))
# print(date_05.to_type_int('40-12-1990'))
