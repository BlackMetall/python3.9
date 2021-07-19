kvart = int(input('Введите квартиру для курьера: '))
etajey = int(input('Введите колличество этажей в подьезде: '))
n = int(input("Введите колличество квартир на этаже: "))
def curier(kvart,etajey,n):
    np = int(1 + (kvart - 1) / (n*etajey))
    ne = int(1 + ((kvart - 1) % (n*etajey)) / n)
    print("Нужная квартира для курьера находится в: " + str(np) + ' подъездe' + ' на ' + str(ne)+ ' этаже')
curier(kvart,etajey,n)



