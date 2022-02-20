while True:
    try:
        x = int (input())
        y = int (input())
        z = input('Введите знак ')

        if z == '+' :
            print (x + y)

        elif z == '-' :
            print(x - y)

        elif z == '*':
            print (x * y)

        elif z == '/':
            print(x / y)

    except ZeroDivisionError:
        print('На ноль делить нельзя! Попробуйте ещё раз!')



