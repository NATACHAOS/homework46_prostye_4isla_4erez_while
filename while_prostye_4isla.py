"""Найти простые числа в диапазоне введённого числа"""

a = int(input("Введите число: ")) # вводим число
flag = True
num = [x for x in range(1, a + 1)] # выведу простые числа от 1 до введённого числа
d = 2
spisok_s_prostymi_4islami = []  # простые числа попадают сюда
while d * d <= a:
    if a % d == 0:
        flag = False
        break
    d += 1
    if flag:   
        spisok_s_prostymi_4islami.append(num)
print(f'{spisok_s_prostymi_4islami} - Простые числа в диапазоне от 1 до {a}')
