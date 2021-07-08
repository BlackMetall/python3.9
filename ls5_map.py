num = int(input('Введите число: '))
def kvadrat(num):
    return num ** 2
lst=[]  #получаем список простых чисел
for num in range(2,num):
    if all(num%i!=0 for i in range(2,num)):
        lst.append(num)     #записываем в список lst полученный список простых чисел от введенного числа
lst_1 = list(map(kvadrat,lst))      #получаем список квадратов списка полученных простых чисел
print("Список простых чисел до введенного числа: " + str(lst))
print('Квадраты списка полученных простых чисел: ' + str(lst_1))



