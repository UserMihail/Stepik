# Дан порядковый номер месяца (1,2,…, 12). Напишите программу,
# которая выводит на экран количество дней в этом месяце.
# Принять, что год является невисокосным.

month = int(input())

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(31)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
elif month == 2:
    print(29)
else:
    print("There is no such month") # Учитываем, что нет нет месяца больше 12