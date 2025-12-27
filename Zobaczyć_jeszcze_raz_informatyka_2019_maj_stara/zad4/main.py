lines = open("dzialki.txt", "r").read().split('\n')
# lines = open("przyklad.txt", "r").read().split('\n')

dzialki = []

dzialka = []
for x in lines:
    if x == '':
        dzialki.append(dzialka)
        dzialka = []
    else:
        dzialka.append(x)

# print(len(dzialki))
#1

# ile = 0
#
# for x in dzialki:
#     trawa = 0
#
#     for wiersz in x:
#
#         for kol in wiersz:
#             if kol == '*':
#                 trawa += 1
#
#
#     if trawa/(30*30)>= 0.70:
#         print(trawa / (30 * 30))
#         ile += 1
#
# print(ile)

#2


# for x in range(len(dzialki)):
#
#     odwrocna = []
#     for a in range(len(dzialki[x]) - 1, -1, -1):
#         yolo = dzialki[x][a]
#         odwrocna.append(yolo[::-1])
#
#
#     for y in range(x + 1, len(dzialki)):
#         if dzialki[y] == odwrocna:
#             print(x + 1, y + 1)

#3

maks = 0
maks_n = 0

i = 0
for x in dzialki:
    i += 1

    ile = 1
    while True:
        czy_git = 1
        for w in range(ile):

            for k in range(ile):
                if x[w][k] == 'X':
                    czy_git = 0
                    break
            if czy_git == 0:
                break

        if czy_git == 0:
            break
        else:
            if ile > maks:
                maks = ile
                maks_n = i
            ile += 1

print(maks, maks_n)

odp = []
i = 0
for x in dzialki:
    i += 1

    ile = 1
    while True:
        czy_git = 1
        for w in range(ile):

            for k in range(ile):
                if x[w][k] == 'X':
                    czy_git = 0
                    break
            if czy_git == 0:
                break

        if czy_git == 0:
            break
        else:
            if ile == maks:
                odp.append(i)
            ile += 1

print(odp)







