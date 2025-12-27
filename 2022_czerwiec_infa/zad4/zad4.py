
import math
lines = open("liczby.txt", "r").read().split()
# lines = open("przyklad.txt", "r").read().split()


def pierw(x):
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
#     odwroc = x[::-1]
#
#     odwroc = int(odwroc)
#
#     if odwroc % 17 == 0:
#         print(odwroc)
#

#2

# maks = 0
# maks_l = 0
#
# for x in lines:
#     odwroc = x[::-1]
#
#     odwroc = int(odwroc)
#
#     if abs(int(x) - odwroc) > maks:
#         maks = abs(int(x) - odwroc)
#         maks_l = x
#
# print(maks_l , maks)

#3

# for x in lines:
#     odwroc = x[::-1]
#     odwroc = int(odwroc)
#
#     if pierw(x) and pierw(odwroc):
#         print(x)

#4

hashmap = {}

for x in lines:
    hashmap[x] = hashmap.get(x, 0) + 1


ile_liczb = len(hashmap)
# print(hashmap)
# print(ile_liczb)

ile_trzy = 0
ile_dwa = 0
for a in hashmap.values():
    if a == 2:
        ile_dwa += 1
    if a == 3:
        ile_trzy += 1

print(ile_liczb, ile_dwa, ile_trzy)