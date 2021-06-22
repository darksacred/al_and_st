from random import randint

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# for i in range(2, 10):
#     s = 0
#     for j in [i for i in range(2, 100)]:
#         if j % i == 0:
#             s += 1
#     print(f'К числу {i} кратны из диапозона (2, 99) столько числе: {s}')

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# m1, m2 = [8, 3, 15, 6, 4, 2], []
# for i, item in enumerate(m1):
#     if item % 2 == 0:
#         m2.append(i + 1)
# print('\t'.join(str(i) for i in m2))

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
# m1 = [randint(1, 100) for i in range(10)]
# print(m1)
# n1 = [i for i, item in enumerate(m1) if item == min(m1)]
# n2 = [i for i, item in enumerate(m1) if item == max(m1)]
# m1[n1[0]], m1[n2[0]] = m1[n2[0]], m1[n1[0]]
# print(m1)

# 4. Определить, какое число в массиве встречается чаще всего.
# m1 = [randint(1, 9) for i in range(10)]
# print(m1)
# max_n = 1
# for i, item in enumerate(m1):
#     n = 0
#     for j in m1:
#         if item == j:
#             n += 1
#     if n > max_n:
#         max_n = n
#         num = m1[i]
# if max_n > 1:
#     print(f'Число {num} встречается {max_n} раз')
# else:
#     print('Все числа уникальны')

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# m1 = [randint(-9, 9) for i in range(10)]
# print(m1)
# for i, item in enumerate(m1):
#     if item == min(m1):
#         n = i + 1
#         break
# print(f'Число {min(m1)}, позиция {n}')


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# m1 = [randint(1, 9) for i in range(10)]
# print(m1)
# n = len(m1)
# sum_row = 0
# for i in range(n):
#     # и тут я вспомнил про подсказку .index()
#     if i == m1.index(min(m1)):
#         m = i
#     if i == m1.index(max(m1)):
#         mx = i
# i = int(m1.index(min(m1)))
# j = int(m1.index(max(m1)))
# if m < mx:
#     for k in range(m+1, mx):
#         sum_row += m1[k]
# else:
#     for k in range(mx + 1, m):
#         sum_row += m1[k]
# print(f'Сумма чисел между минимальным числом и максимальным {sum_row}')

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# m1 = [randint(1, 9) for i in range(10)]
# print(m1)
# n, m2 = 0, []
# for i in m1:
#     if i == min(m1) and n != 2:
#         n += 1
#         m2.append(i)
# print(n)
# if n < 2:
#     for i in m1:
#         if i + 1 == min(m1) + 1:
#             n += 1
#             if n != 3:
#                 m2.append(i+1)
# print(n)
# print(m2)

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# m, n = 5, 4
# m1 = []
# for stroka in range(m):
#     num = list(map(int, input(f'Ведите {stroka + 1} строку чисел: ').split()))
#     m1.append(num)
# for i in m1:
#     s = 0
#     for j in i:
#         s += j
#     m1[m1.index(i)].append(s)
# print('\n'.join(str(i) for i in m1))

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

m, n = 3, 3
m1 = []
m2, m3 = [], []
for stroka in range(m):
    num = [randint(1, 9) for i in range(m)]
    m1.append(num) # Для наглядности
print('\n'.join(str(i) for i in m1))
for i in range(len(m1)):
    for j in range(len(m1)):
        m2.append(m1[j][i])
    m3.append(min(m2))
    m2 = []
print(f'Максимальный элемент из минимальных {max(m3)} в столбце: ')
n = m3.index(max(m3))
for i in range(len(m1)):
    print('\n'.join(str(m1[i][n])))
