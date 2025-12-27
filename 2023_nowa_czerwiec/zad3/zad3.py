from itertools import permutations
lines = open("anagram.txt" , "r").read().split()
# lines = open("przyklad.txt" , "r").read().split()

#1
# zrown = 0
# praw = 0
#
# for x in lines:
#     zero = x.count('0')
#     jeden = x.count('1')
#
#     if abs(jeden - zero) == 0:
#         zrown += 1
#     elif abs(jeden - zero) == 1:
#         praw += 1
#
# print(zrown)
# print(praw)

#2

# for x in lines:
#     if len(x) == 8:
#         zero = x.count('0')
#         jeden = x.count('1')
#
#         if abs(jeden - zero) == 0 or abs(jeden - zero) == 1:
#             print(x)

#drugi sposob z permutations
maks = 0
for x in lines:
    if len(x) == 8:
        perm = permutations(x)
        ile = 0
        perm = set(list(perm))
        for j in perm:
            if j[0] == '1':
                ile += 1

        if ile > maks:
            maks = ile
print(maks)

for x in lines:
    if len(x) == 8:
        perm = permutations(x)
        ile = 0
        perm = set(list(perm))
        for j in perm:
            if j[0] == '1':
                ile += 1

        if ile == maks:
            print(x)

print(set(list(permutations('11'))))
#3

# maks = 0
#
# for x in range(len(lines) - 1):
#     jeden = int(lines[x] , 2)
#     dwa = int(lines[x + 1], 2)
#     # print(jeden, dwa)
#     print(abs(jeden - dwa))
#     if abs(jeden - dwa) > maks:
#
#         maks = abs(jeden - dwa)
#
# maks = bin(maks)
#
# print(maks)

#4

# ile = 0
# maks = 0
# liczba_maks = 0
#
# for a in lines:
#     liczba = int(a, 2)
#     string = str(liczba)
#
#     if string.count('0') == 0:
#         ile += 1
#
#     hashset = set()
#     suma = 0
#     for b in string:
#         b = int(b)
#         if b not in hashset:
#             suma += b
#             hashset.add(b)
#
#     if suma > maks:
#         maks = suma
#         liczba_maks = liczba
#
# print(ile)
# print(liczba_maks)