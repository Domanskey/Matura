import math
# lines = open("dane.txt", "r").read().split()
lines = open("dane_przyklad.txt", "r").read().split()

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
# min = float("inf")
# max = 0
#
# for x in lines:
#     x = int(x)
#     if pierwsza(x):
#         ile += 1
#         if x < min:
#             min = x
#         if x > max:
#             max = x
#
# print(ile, max, min)

#2
# ile = 0
# for x in lines:
#     dw = bin(int(x))
#     dw = dw.lstrip('0b')
#
#     dl = len(dw)
#
#     if dw[0] == '1':
#         if dw == dw[::-1]:
#             ile += 1
#             print(dw)
#         else:
#             for a in range(dl):
#                 dw = '0' + dw
#
#                 if dw == dw[::-1]:
#                     ile += 1
#                     # break
# print(ile)

#3

# print(set('yolo'))
# ile = 0
# for a in range(len(lines)):
#
#     for b in range(a + 1, len(lines)):
#         if set(lines[a]) == set(lines[b]):
#             ile += 1
#
# print(ile)
