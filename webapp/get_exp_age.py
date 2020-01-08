def get_age(age):
    age = int(age)
    if 10 < age < 15:
        return f'{age} лет'
    else:
        i = age % 10
    if i == 1:
        return f'{age} год'
    elif 2 <= i <= 4:
        return f' {age} года'
    else:
        return f' {age} лет'


def get_exp(exp):
    exp = int(exp)
    if 10 < exp < 15:
        return f'{exp} "лет'
    else:
        i = exp % 10
    if i == 1:
        return f'{exp} год'
    elif 2 <= i <= 4:
        return f' {exp} года'
    else:
        return f' {exp} лет'
