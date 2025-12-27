from itertools import permutations

lines = open("anagram.txt", "r").read().split('\n')
# lines = open("przyklad.txt", "r").read().split('\n')

print(lines)

# 1
#
# zr = 0
# pr = 0
#
# for x in lines:
#
#     j = x.count('1')
#     z = x.count('0')
#
#     if j == z:
#         zr += 1
#     elif abs(j - z) == 1:
#         pr += 1
#
# print(zr, pr)

# 2

# maks = 0
#
# for x in lines:
#     if len(x) == 8:
#         perms = set(permutations(x))
#
#         no_0 = []
#         for a in perms:
#             if a[0] == '0':
#                 continue
#             else:
#                 no_0.append(a)
#
#         if len(no_0) > maks:
#             maks = len(no_0)
#
# res = []
#
# for b in lines:
#     if len(b) == 8:
#         perms = set(permutations(b))
#         no_0 = []
#         for c in perms:
#             if c[0] == '0':
#                 continue
#             else:
#                 no_0.append(c)
#
#         if len(no_0) == maks:
#             res.append(b)
#
#
# print(maks)
# for y in res:
#     print(y)

# 3

# maks =0
#
# for a in range(len(lines) - 1):
#     j = int(lines[a], 2)
#     d = int(lines[a + 1], 2)
#     print(j, d)
#
#     if abs(j - d) > maks:
#         maks = abs(j - d)
#
# print()
# print(maks)
# print(bin(maks).lstrip('0b'))


# 4

# a
# ile = 0
#
# for x in lines:
#
#     liczba = int(x, 2)
#
#     liczba = str(liczba)
#
#     ile_zer = liczba.count('0')
#     if ile_zer == 0:
#         ile += 1
#
# print(ile)

# b

# maks = 0
# maks_l = 0
#
# for x in lines:
#     liczba = int(x, 2)
#
#     liczba = str(liczba)
#
#     se = set(liczba)
#     s = 0
#     for a in se:
#         l = int(a)
#         s += l
#
#     if s > maks:
#         maks = s
#         maks_l = liczba
#
# print(maks_l)
)

