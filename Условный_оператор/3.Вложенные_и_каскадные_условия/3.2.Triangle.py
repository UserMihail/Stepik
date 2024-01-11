# Напишите программу, которая принимает три положительных числа и
# определяет вид треугольника, длины сторон которого равны введенным числам.

side1, side2, side3 = int(input()), int(input()), int(input())

if side1 == side2 == side3:
    print("Равносторонний")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Равнобедренный")
else:
    print("Разносторонний")

