# Напишите программу, в которой вычисляется сумма,
# разность и произведение двух целых чисел, введенных с клавиатуры.

print('Enter num: ')
a = int(input())
b = int(input())

s = a + b
s1 = a - b
s2 = a * b

print(f'{a} + {b} = {s}\n{a} - {b} = {s1}\n{a} * {b} = {s2}')

# Напишите программу, которая считывает целое положительное число x
# и выводит на экран последовательность чисел x, 2x..5x   разделённых тремя черточками.

a = int(input())
b = a + a
c = a + b
d = a + c
e = a + d
print(a, b, c, d, e, sep='---')

# ИЛИ

x = int(input())
print(*[ i * x for i in range(1, 6)], sep='---')