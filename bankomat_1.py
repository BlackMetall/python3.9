x  = int(input())
def bankomat (money):
    nominals = [1000,500,200,100,50,20]
    result = []

    if money < 20:
        print('Минимальный номинал куnюры в банкомате -- 20')
        print("Введите число больше 20, но кратно 10")

    if money > 0:
        for i in nominals:
            while money - i >= 0:
                money -= i
                result.append(i)

    else:
        print('Pls enter new amount')

    return result
print(bankomat(x))