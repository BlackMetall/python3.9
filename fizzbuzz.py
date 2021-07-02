from sys import argv
script, filename = argv
txt = open(filename)


fizz = int(input('Введите fizz: '))
buzz = int(input('Введите buzz: '))
c = int(input('Введите число до которого нужно досчитать: '))
for c in range(1, c+1):
    if c%fizz == 0 and c%buzz == 0:
        print('FB', end=' ')
    elif c % fizz == 0:
        print('F', end=' ')
    elif c % buzz == 0:
        print('B', end=' ')
    else:
        print(c, end=' ')

