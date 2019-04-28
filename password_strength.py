import re
from getpass import getpass


def has_lower_case(password):
    return bool(re.search(r'[a-z]', password))


def has_upper_case(password):
    return bool(re.search(r'[A-Z]', password))


def has_numbers(password):
    return bool(re.search(r'[0-9]', password))


def has_special_characters(password):
    return bool(re.search(r'\W', password))


def has_number_phone(password):
    pattern = r'\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d'
    return bool(re.search(pattern, password))


def has_email(password):
    return bool(re.search(r'[0-9a-z-\.]+\@[0-9a-z-]{2,}\.[a-z]{2,}', password))


def get_password_strength(password):
    verification_functions = [
        len(password) >= 8,
        has_lower_case(password),
        has_upper_case(password) * 2,
        has_numbers(password) * 2,
        has_special_characters(password) * 2,
        (not has_number_phone(password)) * 1,
        (not has_email(password)) * 1
    ]
    password_complexity = sum(verification_functions)
    return password_complexity


def main():
    max_bal = 10
    password = getpass('Please enter your password: ')
    password_complexity = get_password_strength(password)
    print('Password complexity {} out of {}'.format(password_complexity,
                                                    max_bal
                                                    )
          )


if __name__ == '__main__':
    main()
