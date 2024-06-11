"""Найти простые числа в диапазоне введённого числа"""
n = int(input())    # вводим число
a = range(1, n + 1)
flag = True   # если число простое, то True
d = 2
prostye_4isla_v_spiske = []   # список, куда попадут простые числа
while d * d <= n:   # пока квадрат переменной меньше или равен введённому числу:
    if n % d == 0:  # если делится на переменную без остатка, то оно не подходит
        flag = False
        break
    d += 1  # проверяем следующее число
if flag:
    rez = prostye_4isla_v_spiske.append(a)
    print(rez)
