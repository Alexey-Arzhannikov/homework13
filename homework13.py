def test(*args, **kwargs):
    print('Позиционные аргументы: ', args)
    print('Именованные аргументы: ', kwargs)


test(1, 'тест', True, t=90, b='класс', c=False)


def factorial(n, x=1):
    if n == 0:
        return x
    else:
        return factorial(n-1, n*x)


print('Факториал заданного числа =  ', factorial(5))
