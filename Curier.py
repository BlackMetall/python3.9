# def curier(kvart):
# kvart = int(input('Введите квартиру для курьера: ')) # кол-во квартир
# pod = int(5)  # кол-во подъездов
# etajey = int(5)  # кол-во этажей
# n = int(4)  # кол-во квартир на этаже
# # В одном подъезде квартир
# n1 = n*etajey
# # Номер подъезда
# np = 1 + (kvart - 1) / n1
# np = int(np)
# print(str(np) + ' подъезд')
# # Номер этажа
# ne = 1 + ((kvart - 1) % n1) / n
# ne = int(ne)
# print(str(ne) + ' этаж')
#
# print("Нужная квартира для курьера находится в: " + str(np) + ' подъездe' + ' на ' + str(ne)+ ' этаже')

# kBaptup_dano = int(71)  # кол-во квартир
# # 57-60 - 5этаж  61-64 - 1этаж  65-68 - 2этаж  69-72 - 3этаж  73-76 - 4этаж  77-80 - 5этаж
# podezd = int(5)  # кол-во подъездов
# etaj = int(5)  # кол-во этажей
# kBaptup_Ha_Etaje = int(4)  # кол-во квартир на этаже
# kBaptup_B_podezde = etaj * kBaptup_Ha_Etaje  # кол-во квартир в подъезде
# uckombIy_podezd = kBaptup_dano // kBaptup_B_podezde  # колличество вхождений квартир на одном этаже в колличество квартир заданное 60//20=3
# uckombIy_podezd_1 = (uckombIy_podezd + 1) # узнаём в каком подъезде квартира
# octatok_kBaptup = kBaptup_dano % kBaptup_B_podezde
# if octatok_kBaptup == 0:
#     print(str(uckombIy_podezd) + ' подъезд')
# else:
#     print(str(uckombIy_podezd_1) + ' подъезд')
#
# d = octatok_kBaptup // kBaptup_Ha_Etaje
# s = (d+1) # узнаём на каком этаже
#
# octatok_kBaptup_1 = int(kBaptup_B_podezde/kBaptup_Ha_Etaje)
# # octatok_kBaptup_1 =
# if octatok_kBaptup == 0:
#     print("Пятый этаж")
# # if 2>s:
# #     print("Первый этаж")
# elif d:  #octatok_kBaptup%4 == 0
#     print(str(d) + ' этаж')
# # else:
# #     print(str(s) + ' этаж')
#
#
# # print(octatok_kBaptup_1)
# print(d)
# print(s)
# # print(octatok_kBaptup_1)
# # print(octatok_kBaptup)
# # print(str(s) + ' этаж')

kvart = int(input('Введите квартиру для курьера: '))
def curier(kvart,etajey,n):
    np = int(1 + (kvart - 1) / (n*etajey))
    ne = int(1 + ((kvart - 1) % (n*etajey)) / n)
    print("Нужная квартира для курьера находится в: " + str(np) + ' подъездe' + ' на ' + str(ne)+ ' этаже')
curier(kvart,5,4)



