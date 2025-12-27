lines = open("liczby.txt", "r").read().split()
# lines = open("przyklad.txt", "r").read().split()
print(lines)

#1
# ile = 0
# nie = 1
# liczba = 0
#
# for x in lines:
#     if x[0] == x[-1]:
#         ile += 1
#         if nie:
#             liczba = x
#             nie = 0
#
# print(ile, liczba)

#2
#
# def rozklad(x):
#     x = int(x)
#     res = []
#     i = 2
#     while x > 1:
#         if x % i == 0:
#             res.append(i)
#             x = x // i
#         else:
#             i += 1
#     return res
#
# l_maks = 0
# maks = 0
# m = []
#
# l_rozn = 0
# rozn = 0
# r = []
#
#
# for x in lines:
#     ile = rozklad(x)
#
#     if len(ile) > maks:
#         maks = len(ile)
#         l_maks = x
#
#     if len(set(ile)) > rozn:
#         rozn = len(set(ile))
#         l_rozn = x
#
# print(l_maks, maks, l_rozn, rozn)
#
# for x in lines:
#     ile = rozklad(x)
#
#     if len(ile) == maks:
#         m.append(x)
#
#     if len(set(ile)) == rozn:
#         r.append(x)
# print(m)
# print(r)
#3

# lines.sort()

# ile = 0
# for x in lines:
#     x = int(x)
#     for y in lines:
#         y = int(y)
#         for z in lines:
#             z = int(z)
#             if x != y and x != z and y!=z:
#                 if y % x == 0 and z % y ==0:
#                     ile += 1
#                     print(x, y, z)
#
# print(ile)

#b

ile = 0

# for u in lines:
#     u = int(u)
#
#     for w in lines:
#         w = int(w)
#         if w == u:
#             continue
#         for x in lines:
#             x = int(x)
#
#             for y in lines:
#                 y = int(y)
#
#                 for z in lines:
#                     z = int(z)
#
#                     if u != w and w != x and x != y and y != z:
#
#                         if w % u == 0 and x % w == 0 and y % x == 0 and z % y == 0:
#                             ile += 1

# for u in lines:
#     u = int(u)
#
#     for w in lines:
#         w = int(w)
#         if w == u:
#             continue
#
#         if w % u == 0:
#             for x in lines:
#                 x = int(x)
#
#                 if x == w or x == u:
#                     continue
#
#                 if x % w == 0:
#
#                     for y in lines:
#                         y = int(y)
#
#                         if y == u or y == w or y == x:
#                             continue
#
#                         if y % x == 0:
#
#                             for z in lines:
#                                 z = int(z)
#
#                                 if z == u or z == u or z == x or z == y:
#                                     continue
#
#                                 if z % y == 0:
#
#                                     if u != w and w != x and x != y and y != z:
#
#                                         if w % u == 0 and x % w == 0 and y % x == 0 and z % y == 0:
#                                             ile += 1
#
# print(ile)
