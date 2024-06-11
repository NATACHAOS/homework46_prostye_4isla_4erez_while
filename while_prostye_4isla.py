"""Найти простые числа в диапазоне введённого числа"""
n = int(input("Простые числа в диапазоне от 1 до: "))  # вводим число

for number in range(1, n + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
