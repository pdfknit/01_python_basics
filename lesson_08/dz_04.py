from functools import wraps


def val_checker(func):
    def logger(callback):
        @wraps(callback)
        def calculate(arg):

            if not func(arg):
                msg = f'wrong val {arg}'
                raise ValueError(msg)
            else:
                return callback(arg)

        return calculate

    return logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    x = 2
    print(f'{calc_cube.__name__}({x}) = {calc_cube(x)}')
