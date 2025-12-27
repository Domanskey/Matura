lines = open("pi.txt", "r").read().split()
# lines = open("pi_przyklad.txt", "r").read().split()

# 1

# ile = 0
#
# for x in range(len(lines) - 1):
#     frag = lines[x] + lines[x + 1]
#
#     liczba = int(frag)
#     if liczba > 90:
#         ile += 1
#
# print(ile)

# 2

# hashmap = [0] * 100
#
# for x in range(len(lines) - 1):
#     frag = lines[x] + lines[x + 1]
#     liczba = int(frag)
#
#     hashmap[liczba] += 1
# print(hashmap)
#
# min = float("inf")
# min_l = 0
# maks = 0
# maks_l = 0
# for a in range(len(hashmap)):
#
#     if hashmap[a] > maks:
#         maks = hashmap[a]
#         maks_l = a
#     if hashmap[a] < min:
#         min = hashmap[a]
#         min_l = a
#
# print(min_l, min, maks_l, maks)


# 3
# ile = 0
# for x in range(len(lines) - 5):
#     a = int(lines[x])
#     b = int(lines[x + 1])
#     c = int(lines[x + 2])
#     d = int(lines[x + 3])
#     e = int(lines[x + 4])
#     f = int(lines[x + 5])
#
#     pop = a
#     tab = [a, b, c, d, e, f]
#     ind = -1
#
#     for j in range(1, len(tab)):
#         if tab[j] <= pop:
#             ind = j
#             break
#
#         pop = tab[j]
#
#     git = 0
#     pop = tab[ind]
#     if ind >= 2:
#         git = 1
#
#         if ind == 5 and tab[ind] == tab[ind - 1]:
#             git = 0
#
#         for c in range(ind + 1, len(tab)):
#             if tab[c] >= pop:
#                 git = 0
#                 break
#
#             pop = tab[c]
#
#     if git == 1:
#         # if ind == 5:
#         #     print(tab, ind)
#
#         ile += 1
#
# print(ile)

#4

tab = [int(x) for x in lines]

maks = -1
maks_s = -1

for x in range(len(tab)):
    pop = tab[x]
    ind = -1

    for j in range(x + 1, len(tab)):
        if tab[j] <= pop:
            ind = j
            break

        pop = tab[j]

    git = 0
    if ind - x >= 2:
        git = 1
        pop = tab[ind]
        last = ind
        for c in range(ind + 1, len(tab)):

            if tab[c] >= pop:
                break

            last = c
            pop = tab[c]

        if last == ind:
            if tab[ind] == tab[ind - 1]:
                git = 0


    if git:
        if last - x > maks:
            maks=  last -x
            maks_s = x

print(maks_s + 1, maks + 1)








