# Напишите программу, которая определяет,
# являются ли три заданных числа (в указанном порядке) последовательными членами

print("Введите три числа: ")
a, b, c = int(input()), int(input()), int(input())

if b-a+b == c:
    print("YES")
else:
    print("NO")