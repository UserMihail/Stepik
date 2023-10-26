# Необязательные параметры команды print

#sep

print('a', 'b', 'c', sep=':)')
print('d', 'e', 'f', sep='**')

# end

print()
print('a', 'b', 'c', end='$')               # end=''- выводит все в одну строку
print('d', 'e', 'f', sep='**', end='\n')    # \n - переход на новую строку

print('a', 'b', 'c', sep=' ')               # sep='' - разделить пробелами

print('python', '\n\n\n')            # Если после вывода данных нужно более одного перевода строки
print('end')

# Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек).

print('I', 'like', 'Python', sep='***')   # три варианта решения задачи
print('I', 'like', 'Python', sep='*'*3)
print('', '', sep='I***like***Python')

