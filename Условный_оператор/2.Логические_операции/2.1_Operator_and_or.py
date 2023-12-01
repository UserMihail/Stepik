age = int(input('Сколько Вам лет? '))
grade = int(input('В каком Вы классе? '))
sity = input('В каком Вы городе? ')

if age >= 12 and grade >= 7 and (sity == 'Москва' or sity == 'Сочи'):
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

