lines = [x.split() for x in open("dane.txt", "r").read().split('\n')]
# lines = [x.split() for x in open("przyklad.txt", "r").read().split('\n')]


#1

# najc = 300
# najj = -5
#
# for w in lines:
#
#     for k in w:
#         k = int(k)
#         if k > najj:
#             najj = k
#         if k < najc:
#             najc = k
#
# print(najj, najc)

#2
# ile = 0
# for w in lines:
#
#
#     s = w[::-1]
#     czy_usunac = 0
#
#     for a in range(len(s)):
#         if s[a] != w[a]:
#             czy_usunac = 1
#             break
#
#     if czy_usunac == 1:
#         ile += 1
#
# print(ile)

#3


# ile = 0
# for a in range(len(lines)):
#
#     for b in range(len(lines[0])):
#
#         czy_kontr = 0
#         if a - 1 >= 0 and abs(int(lines[a - 1][b]) - int(lines[a][b])) > 128:
#             czy_kontr = 1
#
#         if a + 1 <= 199 and abs(int(lines[a + 1][b]) - int(lines[a][b])) > 128:
#             czy_kontr = 1
#
#         if b - 1 >= 0 and abs(int(lines[a][b - 1]) - int(lines[a][b])) > 128:
#             czy_kontr = 1
#
#         if b + 1 <= 319 and abs(int(lines[a][b + 1]) - int(lines[a][b])) > 128:
#             czy_kontr = 1
#
#         if czy_kontr:
#             ile += 1
#
# print(ile)


#4
# ile = 0
# maks = 0
#
# for k in range(len(lines[0])):
#     pop = -4000
#     for w in range(len(lines)):
#         if lines[w][k] == pop:
#             ile += 1
#
#             if ile > maks:
#                 maks = ile
#         else:
#             ile = 1
#         pop = lines[w][k]
#
# print(maks)

#zad 1 sprawdzenie algorytmu

A = [7, 5, 11, 33]
a = 0
b = 0
p = 3

for i in range(len(A)):
    if A[i] % p != 0:
        print(A[i])
        if A[i] > b:
            a = b
            b = A[i]
        else:
            if A[i] > a:
                a = A[i]
print(a, b)
print(a * b)


