from functools import wraps

def val_checker(func):
    @wraps(func)
    def logger(callback):
        @wraps(callback)
        def calculate(arg):

            if not func(arg):
                msg = f'wrong val {arg}'
                raise ValueError(msg)
            else:
                result = callback(arg)
                print(f'{callback.__name__}({arg}) = {result}')

        return calculate

    return logger



@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    import sys

    x = -2
    area_1 = calc_cube(x)
