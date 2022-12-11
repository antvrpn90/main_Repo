def f(x, z, y):
    if z == '+':
        print(x + y)
    elif z == '-':
        print(x - y)
    elif z == '*':
        print(x * y)
    elif z == '/':
        print(x / y)
    elif z == '%':
        print(x % y)
    elif z == '//':
        print(x // y)
    else:
        print('Error')


print('Добро пожаловать в калькулятор')
c = ''
while c != '!':
    print('Введите х')
    x1 = int(input())
    print('Введите + - * / % //')
    z1 = input()
    print('Введите y')
    y1 = int(input())
    f(x1, z1, y1)
    print('Если хотите выйти, нажмите "!" ')
    c = input()

