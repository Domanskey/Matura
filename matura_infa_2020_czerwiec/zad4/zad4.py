import math
lines = [x.split() for x in open("pary.txt", "r").read().split('\n')]
# lines = [x.split() for x in open("przyklad.txt", "r").read().split('\n')]
# print(lines)

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

# for x in lines:
#     liczba = x[0]
#     liczba = int(liczba)
#
#     if liczba % 2 == 0:
#         for a in range(liczba // 2 + 1):
#             p = a
#             d = liczba - a
#
#             if pierwsza(p) and pierwsza(d):
#                 print(f'{liczba} {p} {d}')
#                 break

#2

for x in lines:
    slowo = x[1]

    pop = 0
    dl = 0
    max_dl = 0
    max_l = 0

    for a in slowo:
        if a != pop:
            dl = 1
        else:
            dl += 1

        if dl > max_dl:
            max_dl = dl
            max_l = a
        pop = a
    # if dl == 1:
    #     continue
    print(max_l*max_dl, max_dl)

#3

# min = lines[0]
#
# for x in lines:
#     liczba, slowo = x
#     liczba = int(liczba)
#
#     min_l, min_s = min
#     min_l = int(min_l)
#
#     # print(liczba, slowo, min_l, min_s)
#     if liczba == len(slowo):
#         if liczba < min_l:
#             min = x
#
#         if liczba == min_l:
#             if slowo < min_s:
#                 min = x
#
# print(f'{min[0]} {min[1]}')


