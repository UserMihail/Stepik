# Напишите программу,
# которая считывает три числа и подсчитывает сумму только
# положительных чисел.

a, b, c = int(input()), int(input()), int(input()),
sum = 0

if a > 0:
    sum += a
if b > 0:
    sum += b
if c > 0:
    sum += c
print(sum)