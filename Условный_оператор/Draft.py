n = int(input())

if n == 0:
    print('зеленый')
elif not(0 < n < 37):
    print('ошибка ввода')
elif (0 < n < 11 or 18 < n < 29) - n % 2:
    print('черный')
else:
    print('красный')