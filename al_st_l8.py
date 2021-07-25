# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

# Провести поиск подстроки в строке
import hashlib


def kol_podstrok(s):
    n = 0
    for i in range(len(s)):
        h_subs = hashlib.sha1(s[:i + 1].encode('utf-8')).hexdigest()
        for j in range(len(s)):
            if h_subs == hashlib.sha1(s[j:i + j + 1].encode('utf-8')).hexdigest():
                n += 1
                j += 1
    return n


def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            return i
    return -1


s = 'dfabaabstarawaba'
t = 'aba'
print(f'Строка: {s}')
print(f'Ищем в строке: {t}')
print(f'Кол-во разных подстрок в строке: {kol_podstrok(s)}')
print(f'Первое вхождение по индексу в строке: {rabin_karp(s, t)}')

# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)


def main():
    s = "beep boop beer!"
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)

    print(f'Кол-во закодированных элементов: {len(code)}, Длина закодированной строки: {len(encoded)}')
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)
    print(huffman_decode(encoded, code))


print(main())

# Кол-во закодированных элементов: 7, Длина закодированной строки: 40
#  : 101
# !: 1111
# b: 00
# e: 01
# o: 110
# p: 100
# r: 1110
# 0001011001010011011010010100010111101111
# beep boop beer!

# Делал по примеру, пытаясь разобраться.
