import re


def email_parse(src_email):
    result_list = {'username': '', 'domain': ''}
    # try:
    domain_pattern = re.compile(r'[a-z0–9A-Z_-]+@[a-z0–9A-Z_-]+\.[a-z0–9A-Z_\.-]+')
    print(domain_pattern.search(src_email))

    if domain_pattern.search(src_email) is None:
        msg = f'wrong email: {src_email}'
        raise ValueError(msg)

    pattern = re.split(r'@', src_email)
    result_list['username'] = pattern[0]
    result_list['domain'] = pattern[1]
    print(result_list)


if __name__ == '__main__':
    import sys

    email_parse('kia-ry@mail.spb.ru')
