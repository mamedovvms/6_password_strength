import re


def get_password_strength(password):
    rezult = 0

    for exp in [r'[a-z]', r'[A-Z]', r'[0-9]', r'[@,#,$]']:
        rezult += 1 if re.search(exp, password) else 0
    if re.search(r'.{8,}', password):
        rezult += 2
        for exp in [r'\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)'
                    r'?[- .]?\d\d\d[- .]?\d\d\d\d',
                    r'[0-9a-z-\.]+\@[0-9a-z-]'
                    r'{2,}\.[a-z]{2,}',
                    ]:
            rezult += 2 if not re.search(exp, password) else 0
    return rezult


if __name__ == '__main__':
    password = input('Password: ')
    rezult = get_password_strength(password)
    print('Security', rezult)
