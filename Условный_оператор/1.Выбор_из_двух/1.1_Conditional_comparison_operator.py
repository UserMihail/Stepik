# Условный оператор if-else, и оператор сравнения.

print("Введите число 1: ")
num1 = int(input())
print("Введите число 2: ")
num2 = int(input())

if num1 > num2:
    print(num1, "больше", num2)
if num1 < num2:
    print(num1, "меньше", num2)
if num1 == num2:
    print(num1, "равно", num2)
if num1 != num2:
    print(num1, "не равно", num2)

# Цепочки сравнений

age = int(input())

if 3 <= age <= 6:
    print("Вы ребенок")

