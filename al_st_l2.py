# 1
while True:
    ls = list(input(f'Введите два числа и знак или введите 0 в знаке для выхода: ').split())
    a = int(ls[0])
    b = int(ls[1])
    z = ls[2]
    if z == '0':
        print(f'Программа завершается')
        break
    elif z == '+':
        print(a + b)
    elif z == '-':
        print(a - b)
    elif z == '*':
        print(a * b)
    elif z == '/':
        if b == 0:
            print(f'На 0 делить нельзя, повторите.')
        else:
            print(a / b)
    elif z != '+' or z != "-" or z != '*' or z != '/':
        print(f'Вы ввели не верный знак, повторите.')


# 2
even = []
not_even = []
j = 0
k = 0
ls = list(map(int, input(f'Введите число: ')))
for i in ls:
    if i % 2 == 0:
        even.append(i)
        j += 1
    else:
        not_even.append(i)
        k += 1
print(f'Число имеет {j} чётных числа ({even}) и {k} не чётных числа({not_even})')


# 3
ls = int(input(f'Введите число: '))
ls1 = 0
while ls > 0:
    d = ls % 10
    print(f'{d}')
    ls = ls // 10
    print(f'{ls}')
    ls1 = ls1 * 10
    print(f'{ls1}')
    ls1 = ls1 + d
    print(f'{ls1}')
print(f'Обратное ему: {ls1}')


# 4
ls = int(input(f'Введите число: '))
n = 1
k = 1
d = 1
if ls == 1:
    print(f'Сумма: {k}')
else:
    while n < ls:
        k = k / -2
        d += k
        n += 1
    print(f'Сумма: {k}')


# 5

j = 0
for i in range(32, 128):
    print(f'{(i, chr(i))}', end=' ')
    j += 1
    if j % 10 == 0:
        print()
        j = 0


# 6
import random


def proverka(a, ls):
    if a == ls:
        return print(f'Поздравляю Вы угадали!')
    elif a < ls:
        return print(f'Увы, ваше число меньше')
    elif a > ls:
        return print(f'Увы, ваше число больше')


ls = random.randint(0, 100)
n = 0
b = 0
while n < 10:
    a = int(input(f'Угадайте число от 0 до 100: '))
    proverka(a, ls)
    n += 1
    if a == ls:
        break
    if n == 10:
        print(f'Вы проиграли, число было {ls}')
        break


# 7
#Не совсем понял задачу.. но вот:
def number(n):
    s = n * (n + 1) / 2
    return print(f'Равенство n(n+1)/2 выполняется, ответ {s}')


while True:
    n = int(input(f'Введите любое натуральное число или 666 для выхода: '))
    if n != 666:
        number(n)
    else:
        break


# 8
n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input(f'Число {i}: '))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print(f'Было введено {count} c цифрой {d}')

# 9

n = int(input("Сколько будет чисел? "))
count = 0
ls = []
ls1 = []
for i in range(1, n + 1):
    m = int(input(f'Число {i}: '))
    ls.append(m)
    s = 0
    while m > 0:
        d = m % 10
        s += d
        m = m // 10
    ls1.append(s)

a = max(ls1)
for i, item in enumerate(ls1):
    if item == a:
        b = ls[i]

print(f'Самое большое число {max(ls1)} по сумме цифр {b}')