kvart = int(input('Введите квартиру для курьера: '))
def curier(kvart,etajey,n):
    np = int(1 + (kvart - 1) / (n*etajey))
    ne = int(1 + ((kvart - 1) % (n*etajey)) / n)
    print("Нужная квартира для курьера находится в: " + str(np) + ' подъездe' + ' на ' + str(ne)+ ' этаже')
curier(kvart,5,4)



