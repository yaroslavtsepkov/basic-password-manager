import string
import numpy as np

def header():
    print('-'*72)
    print('-'*16,"Hello this is your password manager",'-'*16)

def menu():
    print('Options: [1] - create user')
    print('Options: [2] - create record')
    print('Options: [3] - get records by user')
    print('Options: [4] - dump to file')
    print('Options: [5] - set config')

def genPassword():
    words = list(string.ascii_letters+string.digits)
    password = ''.join(np.random.choice(words, 16))
    return password

