import math
lines = [x.split() for x in open("punkty.txt", "r").read().split('\n')]

print(lines)

def pierwsza(x):
    x = int(x)
    if x < 2:
        return False
    if x == 2:
        return True
    for a in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % a == 0:
            return False

    return True

#1

# ile = 0
#
# for x, y in lines:
#
#     if pierwsza(x) and pierwsza(y):
#         print(x, y)
#         ile += 1
# print(ile)

#2

# ile = 0
# for x, y in lines:
#
#     first = set(list(x))
#     second = set(list(y))
#     # print(first, second)
#     if first == second:
#         print(first, second)
#         ile += 1
#
# print(ile)

#3

# maks = 0
# ma = 0
# mb = 0
#
# for a in range(len(lines)):
#     xa = int(lines[a][0])
#     ya = int(lines[a][1])
#
#     for b in range(a + 1, len(lines)):
#         xb = int(lines[b][0])
#         yb = int(lines[b][1])
#
#         dl = round( math.sqrt( (xb- xa) ** 2 + (yb - ya) **2 ) )
#
#         if dl > maks:
#             maks = dl
#             ma = lines[a]
#             mb = lines[b]
#
# print(maks, ma, mb)


#4a
# a = 0
# for x, y in lines:
#     x = int(x)
#     y = int(y)
#
#     if x < 5000 and x > -5000 and y < 5000 and y > -5000:
#         a += 1
#
# print(a)

#4b
# b = 0
# for x, y in lines:
#     x = int(x)
#     y = int(y)
#
#     if x == 5000 or x == -5000:
#         b += 1
#     elif y == 5000 or y == -5000:
#         b += 1
#
# print(b)

#4c
# c = 0
# for x, y in lines:
#     x = int(x)
#     y = int(y)
#
#     if x > 5000 or x < -5000:
#         c += 1
#
#     elif y > 5000 or y < -5000:
#         c += 1
#
# print(c)

