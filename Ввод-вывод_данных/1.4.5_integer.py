# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
# Напишите программу, которая определяет номер купе, в котором находится место
# с заданным номером (нумерация мест сквозная, начинается с 1.

num = int(input())
num_2 = (num + 3) // 4 # поскольку мест 4, то добавляем 3 для целочисленного деления
print(num_2)