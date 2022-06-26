'''
Внешние функции для бота
'''


def get_token(file):
    with open(file,'r') as f:
        return f.read()

