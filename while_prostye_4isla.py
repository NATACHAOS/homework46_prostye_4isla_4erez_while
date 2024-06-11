"""Найти простые числа в диапазоне введённого числа"""

a = int(input("Введите число: "))
flag = True
num = [x for x in range(1, a + 1)]
d = 2
spisok_s_prostymi_4islami = []
while d * d <= a:
    if a % d == 0:
        flag = False
        break
    d += 1
else:
    spisok_s_prostymi_4islami.append(num)
print(f'{spisok_s_prostymi_4islami} - Простые числа в диапазоне от 1 до {a}')
