# Декораторы

def outer():
    x = 5

    def inner():
        nonlocal x
        print('NonLocal x=', x)
        x= 10
    inner()
    print('New x=', x)
outer()

def logger(func):
    counter = 0
    def decor_func(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(counter, '->', 'Argumenty: ', args, 'Imenovan argumenty: ', kwargs)
        result = func(*args, **kwargs)
        print('____', 'REsult: ', result)
        return result
    return decor_func()

@logger
def make_burger(meal='Pork', onion=False, tomat=False):
    print('Bulochka')
    if onion:
        print('LookLook')
    print('Kotleta s', meal)
    if tomat:
        print('Tomat`s')

make_burger(onion=True)

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultat = func(*args, **kwargs)
        finish = time.time()
        print(f'Выполнялась: {finish - start:.4f} sek.')
        return resultat
    return wrapper

@timeit
def test():
    time.sleep(0.8)

test()