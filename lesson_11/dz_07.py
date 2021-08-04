import re


class Complex:
    def __init__(self, digit):
        self.digit = self._validator(digit)

    @staticmethod
    def _validator(digit):
        # digit_pattern = re.compile(r'([-]*\d+[+-]\d+[i])|(\d+[i])|([-]\d+[i])|(\d+[i][+-]\d+)')
        digit_pattern = re.compile(r'([-]*\d+\.*\d*[+-])\d*\.*\d*[i]')
        if digit_pattern.search(digit) is None:
            raise ValueError('wrong digit format')
        else:
            return digit

    def separate_parts(self):
        real_part_pattern = re.compile(r'([-]*\d+\.*\d*[^i])')
        real_part = re.findall(real_part_pattern, self.digit)
        complex_part_pattern = re.compile(r'[-]*\d*\.*\d*[i]')
        complex_part = re.findall(complex_part_pattern, self.digit)
        return float(real_part[0][:-1]), float(complex_part[0].strip('i'))

    def __str__(self):
        return f"{self.digit}"

    def __add__(self, other):
        self_real_part, self_complex_part = self.separate_parts()
        other_real_part, other_complex_part = other.separate_parts()
        final_real_part = self_real_part + other_real_part
        final_complex_part = self_complex_part + other_complex_part
        if final_complex_part >= 0:
            final_digit = f'{round(final_real_part, 3)}+{final_complex_part}i'
        else:
            final_digit = f'{round(final_real_part, 3)}{final_complex_part}i'

        return Complex(final_digit)

    def __mul__(self, other):
        self_real_part, self_complex_part = self.separate_parts()
        other_real_part, other_complex_part = other.separate_parts()
        final_real_part = self_real_part * other_real_part
        final_complex_part = self_complex_part * other_complex_part
        if final_complex_part >= 0:
            final_digit = f'{round(final_real_part, 3)}+{final_complex_part}i'
        else:
            final_digit = f'{round(final_real_part, 3)}{final_complex_part}i'

        return Complex(final_digit)


digit_01 = Complex('-3.3+2i')
digit_02 = Complex('2-3i')

print(digit_01)
print(digit_02)
print(digit_01 + digit_02)
print(digit_01 * digit_02)
