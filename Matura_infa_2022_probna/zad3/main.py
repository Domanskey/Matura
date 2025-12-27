import math
# lines = open("liczby.txt", "r").read().split()
lines = open("liczby_przyklad.txt", "r").read().split()

# def czy_pierwsza(x):
#     x = int(x)
#     if x < 2:
#         return False
#     if x == 2:
#         return True
#     for a in range(2, math.ceil(math.sqrt(x)) + 1):
#         if x % a == 0:
#             return False
#
#     return True

def czy_pierwsza(x):
    czynnik = 2

    if x < 2:
        return False

    while czynnik*czynnik <= x:
        if x % czynnik == 0:
            return False
        else:
            czynnik += 1
    return True

#2

# ile = 0
# for x in lines:
#     if czy_pierwsza(int(x) - 1):
#         ile += 1
#
# print(ile)

#3
# pierwsze = []
# for x in range(1000000 + 6):
#     if czy_pierwsza(x):
#         pierwsze.append(x)
#
# print(pierwsze)
# maks = 0
# jaka_maks = 0
#
# min = float("inf")
# jaka_min = 0
#
# for x in lines:
#
#     x = int(x)
#
#     if x % 2== 0:
#         polowa = x // 2
#
#         ile = 0
#
#         for y in range(1, polowa + 1):
#             first = y
#             second = x - first
#
#             if first in pierwsze and second in pierwsze:
#                 ile += 1
#
#
#         if ile > maks:
#             maks = ile
#             jaka_maks = x
#
#         if ile < min :
#             min = ile
#             jaka_min = x
#
# print(jaka_maks, maks)
# print(jaka_min, min)


#4
# hashmap = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
# for x in lines:
#     x = int(x)
#     sz = hex(x)
#     sz = str(sz.lstrip("0x"))
#     for y in sz:
#         hashmap[y] = hashmap.get(y, 0) + 1
#
# print(hashmap)


#3
lines = open("liczby.txt", "r").read().split()
# lines = open("liczby_przyklad.txt", "r").read().split()

# print(max(lines))
def sito(N):
    T = [True for n in range(0, N+1)]
    for n in range(2, N + 1):
        if T[n] == True:
            for j in range(n*n, N+1, n):
                T[j] = False
    return T

prime = sito(1000000)

max_r = 0
max_x = 0
min_x = 0
min_r = float("inf")

for x in lines:
    x = int(x)
    a = 2
    b = x - a
    ile_r = 0
    while a <= b:
        if prime[a] == True and prime[b] == True:
            ile_r += 1
        a += 1
        b = x - a
    if ile_r > max_r:
        max_r = ile_r
        max_x = x
    if ile_r < min_r:
        min_r = ile_r
        min_x = x

print(max_x, max_r, min_x, min_r)
