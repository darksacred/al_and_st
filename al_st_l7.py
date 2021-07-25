# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def bubble_sort(ls):
    n = 1
    while n < len(ls):
        for i in range(len(ls) - 1):
            if ls[i] < ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
        n += 1


ls = [random.randint(-100, 100) for _ in range(10)]
print(ls)
bubble_sort(ls)
print(ls)


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    mid = len(ls) // 2
    left = merge_sort(ls[:mid])
    right = merge_sort(ls[mid:])
    return merge(left, right)


def merge(left, right):
    sorted_list = []  # Список для сбора
    left_index = right_index = 0  # Индексы списка
    left_len, right_len = len(left), len(right)  # Длина списка

    for _ in range(left_len + right_len):
        if left_index < left_len and right_index < right_len:
            if left[left_index] <= right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1
        elif left_index == left_len:
            sorted_list.append(right[right_index])
            right_index += 1
        elif right_index == right_len:
            sorted_list.append(left[left_index])
            left_index += 1
    return sorted_list


ls = [random.uniform(0, 50) for _ in range(10)]
print(ls)
print(merge_sort(ls))
print(["%.3f" % _ for _ in merge_sort(ls)])  # Хотел число уменьшить

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках


import statistics

array = [random.randint(0, 50) for _ in range(2 * int(random.randint(0, 6)) + 1)]

print(statistics.median(array))  # Как вариант, один из методов

# Тут попытался сам придумать поиск
n = 0
for i in array:
    ln = (len(array) // 2)
    j = 0
    count = 0
    count_d = 0
    for j in range(len(array)):
        if i > array[j]:
            count += 1
        if i == array[j]:
            count_d += 1
    if count == ln:
        n = i
        break
    if count_d % 2 == 0:
        count += (count_d // 2)
        if count == ln:
            n = i
            break
    elif count_d % 2 != 0:
        count += count_d - 1
        if count == ln:
            n = i
            break
print(array)
print(n)

# Ещё один маленький вариант
array = sorted(array)
i = len(array) // 2
print(array)
print(array[i])
print(array.index(array[i]))
