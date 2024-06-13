"""Найти простые числа в диапазоне введённого числа"""

while True:
    diapazon = int(input("Введите диапазон для поиска простых чисел от 1 до: "))
    for num in range(2, diapazon):
        count = 0
        delitel = 2
        while delitel < num:
            if num % delitel == 0:
                count += 1
            delitel += 1
        if count == 0:
            print(f'{num} простое число')
    else:
        break
