from functools import reduce

# №1
a = list(map(int, input(f'Введите два трёхзначных числа: ').split()))
k = 0
for i in a:
    l = len(str(i))
    if l != 3:
        break
    else:
        k += 1
if k != 2 or l != 3:
    print(f'Вы ввели не верные значение(я)')
else:
    print(sum(a))
    print(reduce(lambda x, y: x * y, a))


# №2
a = 5
b = 6
# # ~ – битовый оператор НЕТ (инверсия, наивысший приоритет);
# # <<, >> – операторы сдвига влево или сдвига вправо на заданное количество бит;
# # & – битовый оператор И (AND);
# # ^ – битовое исключающее ИЛИ (XOR);
# # | – битовый оператор ИЛИ (OR).
print(bin(a))  # 0b101
print(bin(~a))  # -0b110
print(bin(b))  # 0b110
print(bin(~b))  # -0b111

print(bin(a << 2))  # 0b10100 - a*2**n n - число смещения
print(bin(a >> 2))  # 0b1 - a/2**n n - число смещения
print(a << 2)  # 20
print(a >> 2)  # 1

z = a & b
print(bin(a))  # 0b101
print(bin(b))  # 0b110
print(bin(z))  # 0b100 - 4

z = a ^ b
print(bin(a))  # 0b101
print(bin(b))  # 0b110
print(bin(z))  # 0b11 - 3

z = a | b
print(bin(a))  # 0b101
print(bin(b))  # 0b110
print(bin(z))  # 0b111 - 7


# №3
print(f'Первая координата')
x1 = int(input(f'Введите x: '))
y1 = int(input(f'Введите y: '))
print(f'Вторая координата')
x2 = int(input(f'Введите x: '))
y2 = int(input(f'Введите y: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'Уравнение прямой вида y=kx+b проходящей через эти точки: y = {k}*x + {b}')


# №4
import string
import random

a = list(map(int, input(f'Введите границы для случайного числа: ').split()))
b = list(map(float, input(f'Введите границы для случайного вещественного числа: ').split()))
c = list(map(str, input(f'Введите границы для случайного символа: ').split()))
print(f'Случайное число: {random.randint(a[0], a[1])}')
print(f'Случайное вещественное число: {str(random.uniform(b[0], b[1]))[:4]}')
list_st = string.ascii_letters
n1 = [i for i, item in enumerate(list_st) if item == c[0]]
n2 = [i for i, item in enumerate(list_st) if item == c[1]]
n = random.randint(n1[0], n2[0])
print(f'Случайный символ: {list_st[n]}')


# №5
a = list(map(str, input(f'Введите границы для случайного символа: ').split()))
list_st = string.ascii_lowercase
n1 = [i for i, item in enumerate(list_st) if item == a[0]]
n2 = [i for i, item in enumerate(list_st) if item == a[1]]
print(f'Позиция первой буквы: {n1[0]+1}, позиция второй буквы: {n2[0]+1}')
if n2[0] == 0 or n2[0] == 1:
    k = 0
    print(f'Между ними нет букв')
else:
    k = 1
    print(f'Между ними {n2[0]-k} букв')


# №6
a = input(f'Введите номер буквы: ')
list_st = string.ascii_lowercase
n1 = [item for i, item in enumerate(list_st) if i == int(a)]
print(f'Под этим номером буква: "{n1}"')

# №7
a = int(input(f'Введите длину отрезка А: '))
b = int(input(f'Введите длину отрезка B: '))
c = int(input(f'Введите длину отрезка C: '))
if a != 0 and b != 0 and c != 0:
    print(f'Такой треугольник существует')
    if a != b and a != c and b != c:
        print(f'Это разносторонний треугольник')
    elif a == b and a == c and b == c:
        print(f'Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print(f'Треугольник равнобедренный')
else:
    print(f'Увы, такого треугольника не бывает')


# №8
# делиться без остатка на 4 и при этом не делиться на 100,
# либо же просто делиться без остатка на 400.
a = int(input(f'Для определения високосного года введите год: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'Год высокосный')
else:
    print(f'Год невысокосный')


# №9
a = list(map(int, input(f'Введите три числа: ').split()))
a.sort()
print(a)
n = [item for i, item in enumerate(a) if item > min(a) and item < max(a)]
print(f'Среднее число из введённых: {n}')
