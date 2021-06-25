import timeit
import random
import cProfile

# 1.
# 3.4. Определить, какое число в массиве встречается чаще всего.
# def number():
#     m1 = [random.randint(1, 9) for i in range(1000)]
#
#     max_n = 1
#     for i, item in enumerate(m1):
#         n = 0
#         for j in m1:
#             if item == j:
#                 n += 1
#         if n > max_n:
#             max_n = n
#             num = m1[i]
#     if max_n > 1:
#         return print(f'Число встречается раз')
#     else:
#         return print('Все числа уникальны')


# При [random.randint(-9, 9) for i in range(10)]
##print(timeit.timeit('number', 'from al_st_l4 import number'))
# 0.010528200000000001 10
# 0.010247599999999996 1000
# 0.013299100000000005 10000
##cProfile.run('number()')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 al_st_l4.py:8(number) 10
#         1    0.022    0.022    0.023    0.023 al_st_l4.py:8(number) 1000
#         1    2.335    2.335    2.350    2.350 al_st_l4.py:8(number) 10000

# Сложность: O(2^n) - т.к. при увеличении количество элементов в 100 (Третья попытка только в 10 удалась) раз,
# увеличивает время выполнения в 100 раз.

# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# Не сделал.


# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;

# def number(n):
#     count = 1
#     count_n = 1
#     lst = [2]
#     if n == 1:
#         return 2
#
#     while count != n:
#         count_n += 2
#
#         for i in lst:
#             if count_n % i == 0:
#                 break
#         else:
#             count += 1
#             lst.append(count_n)
#     return count_n


# print(number(4))
# print(timeit.timeit('number(1)', 'from al_st_l4 import number'))
# print(timeit.timeit('number(5)', 'from al_st_l4 import number'))
# print(timeit.timeit('number(10)', 'from al_st_l4 import number'))
# 0.0976717
# 0.9541855
# 3.1476981

# cProfile.run('number(10)')
# cProfile.run('number(100)')
# cProfile.run('number(1000)')
#        1    0.000    0.000    0.000    0.000 al_st_l4.py:46(number)
#        1    0.000    0.000    0.000    0.000 al_st_l4.py:46(number)
#        1    0.018    0.018    0.018    0.018 al_st_l4.py:46(number)
#Сложность: O(n^2) т.к. время выполнения растёт в 10 раз.

# C использованием «Решета Эратосфена»;
def number(n):
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    return a

# print(timeit.timeit('number(1)', 'from al_st_l4 import number'))
# print(timeit.timeit('number(5)', 'from al_st_l4 import number'))
# print(timeit.timeit('number(10)', 'from al_st_l4 import number'))
# 0.5919098
# 1.1297888
# 1.9342547000000003
# cProfile.run('number(100)')
# cProfile.run('number(1000)')
# cProfile.run('number(10000)')
#        1    0.000    0.000    0.000    0.000 al_st_l4.py:82(number)
#        1    0.000    0.000    0.000    0.000 al_st_l4.py:82(number)
#        1    0.003    0.003    0.004    0.004 al_st_l4.py:82(number)
#Сложность: O(n^2) т.к. время выполнения растёт в 10 раз.
#Но использованием «Решета Эратосфена» выполняется в 4.5 раза быстрее

# Не уверен в правильности решении этих задач, нужно больше разбора.