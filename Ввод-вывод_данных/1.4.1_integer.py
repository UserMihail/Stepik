'''
Тема урока: работа с целыми числами
'''

# Преобразование типов

s = '1992'
year = int(s)   # Преобразовали строку в число
print(year, type(year))

num = 17
st = str(num)   # Преобразовали число в строку
print(st, type(st))


# Напишите программу вывода на экран трех последовательно идущих чисел,
# каждое на отдельной строке. Первое число вводит пользователь,
# остальные числа вычисляются в программе.

num = int(input())
print(num, num + 1, num + 2, sep='\n')   # разделяем переходом на новую строку

# Напишите программу, которая считывает три целых числа и выводит на экран их сумму.
# Каждое число записано в отдельной строке.

print(int(input()) + int(input()) + int(input()))