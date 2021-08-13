#                     praktika_1

stud = {'John Malkov': 80, 'Abraham Ronny': 90, 'Nikas Armstrong': 100, 'Gosha Kucenko': 150}
n = stud.keys()
n = len(n)
point = sum(stud.values())
midlle_point = point / n
print("Средний балл студентов: " + str(int(midlle_point)))
print('Студенты с баллом выше среднего: ')
for i in stud:
    if stud[i] > midlle_point:
        print(i)
print("Студенты с баллом ниже среднего:")
for i in stud:
    if stud[i] < midlle_point:
        print(i)

# ===========================================================================

#                    praktika_2
all_stydents = {'John Malkov', 'Abraham Ronny', 'Jack Russel', 'Robert Ford', 'The Rock', 'Illia Golem',
                'Nikas Armstrong', 'Markus Ruhll', 'Gosha Kucenko'}
Python = {'John Malkov', 'Jack Russel', 'Illia Golem', 'Nikas Armstrong'}
FrontEnd = {'Abraham Ronny', 'Robert Ford', 'John Malkov'}
FullStack = {'Markus Ruhll', 'Nikas Armstrong', 'The Rock', 'Jack Russel'}
Java = {'Gosha Kucenko', 'Nikas Armstrong', 'Robert Ford'}

print('\nСтуденты которые обучаются в двух и более группах: ' + str(
    (Python & FrontEnd) |
    (Python & FullStack) |
    (Python & Java) |
    (FrontEnd & FullStack) |
    (FrontEnd & Java) |
    (FullStack & Java)))

print('Студенты не изучающие FrontEnd: ' + str(list(all_stydents - FrontEnd)))

print('Студенты которые изучают Python и Java: ' + str(list(Python | Java)))




