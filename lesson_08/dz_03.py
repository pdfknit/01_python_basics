from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        cube = func(*args)
        types = (f'{x}: {type(x)}' for x in args)
        all_types = ', '.join(types)
        print(f'{func.__name__} ({all_types})')
        return cube

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def args_calc_cube(x, y):
    return x ** 3


if __name__ == '__main__':
    import sys

    x = 12
    area_1 = calc_cube(x)
    args_calc_cube(12, 'Хэй')


