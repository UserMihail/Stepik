# Напишите программу, которая определяет, является число четным или нечетным

num = int(input())
if num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

# Или
print(('Четное','Нечетное')[ int(input()) % 2 ])

# Или
x = int(input())
y = x % 10
if y == 0 or y == 2 or y == 4 or y == 6 or y == 8:
    print('Четное')
else:
    print('Нечетное')
