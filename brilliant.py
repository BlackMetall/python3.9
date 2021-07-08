brilliant = int(input())

if brilliant %2==0:
    for i in range(brilliant + 1):
        up = brilliant - i
        print (' ' * up + '* ' * i)
    for i in range(brilliant-1, 0, -1):
        down = brilliant - i
        print(' ' * down + '* ' * i)
if brilliant %2 ==1 :
    for i in range (1, brilliant, 2):
        i = ' ' * ((brilliant - i) // 2) + '*' * i + ' ' * (brilliant - i)
        print(i)
    for i in range(brilliant, 0, -2):
        i = ' ' * ((brilliant - i) // 2) + '*' * i + ' ' * (brilliant - i)
        print(i)







# if total == 1:
#     for i in range(total+1):
#         up = total + i
#         print(' ' * up + '* ' * i)
# if total %2!=0:
#     for i in range (total+1):
#         up = total - i
#         print(' ' * up + '* ' * i )