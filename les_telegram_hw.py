stud= {'Годунов Никита': {'схема':4, 'fb':6, 'fb+':6, 'practicka1':10,'string':0, 'dict':0, 'git1':6, 'practicka2':10, 'module':10},
       'Гоптарев Денис': {'схема':6, 'fb':10, 'fb+':0, 'practicka1':10,'string':0, 'dict':0, 'git1':0, 'practicka2':10, 'module':10},
       'Дзядух Юрий': {'схема':7, 'fb':8, 'fb+':8, 'practicka1':10,'string':0, 'dict':0, 'git1':8, 'practicka2':10, 'module':10},
       'Кальченко Владислав': {'схема':7, 'fb':8, 'fb+':8, 'practicka1':10,'string':0, 'dict':0, 'git1':8, 'practicka2':10, 'module':10},
       'Лисицкий Владимир': {'схема':7, 'fb':10, 'fb+':8, 'practicka1':10,'string':8, 'dict':8, 'git1':8, 'practicka2':10, 'module':10},
       'Савченко Владимир': {'схема':8, 'fb':10, 'fb+':9, 'practicka1':10,'string':8, 'dict':8, 'git1':8, 'practicka2':10, 'module':10},
       'Трофимчук Владимир': {'схема':8, 'fb':10, 'fb+':10, 'practicka1':10,'string':9, 'dict':10, 'git1':8, 'practicka2':10, 'module':10},
       'Коршунов Дмитрий': {'схема':7, 'fb':10, 'fb+':10, 'practicka1':10,'string':10, 'dict':10, 'git1':10, 'practicka2':10, 'module':10},
       }


for student in stud:
    s = 0
    for work in stud[student]:
        s+=stud[student][work]
    s = s/len(stud[student])
    if s<6:
        print('========================================================')
        print(f'Самый не успешный ученик: {student} с оценкой: {int(s)}')
        print('========================================================')
    print(f'Студент: {student}, средняя оценка -> {int(s)}')
    for work,values in stud[student].items():
        if values < 5:
            print(f'У студента: {student} проблемы с темой: {work}')

