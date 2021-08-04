class OnlyDigitError(ValueError):
    pass


digit_list = []
stops = True
while stops:
    arg = input('Введите число или stop:\n')
    if arg == 'stop':
        stops = False
        print(digit_list)
    else:
        try:
            try:
                if arg.isdecimal():
                    arg = int(arg)
                else:
                    arg = float(arg)
            except ValueError:
                raise OnlyDigitError
        except OnlyDigitError:
            print('Необходимо ввести число')
        else:
            digit_list.append(arg)
