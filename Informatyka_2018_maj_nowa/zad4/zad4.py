lines = open("sygnaly.txt", "r").read().split()
# lines = open("przyklad.txt", "r").read().split()

#1

# i = 40
#
# res = ""
# while i - 1 < len(lines):
#     res += lines[i - 1][9]
#
#     i += 40
#
# print(res)

#2

# maks = 0
# maks_s = 0
#
# for x in lines:
#     litery = set(x)
#     if len(litery) > maks:
#         maks = len(litery)
#         maks_s = x
#
# print(maks_s, maks)

#2 druga wersja

# maks = 0
# maks_s = 0
#
# print(ord("Z"))
# for x in lines:
#     tab = [0]*101
#     for a in x:
#         tab[ord(a)] += 1
#     # print(tab)
#     ile = 0
#     for b in tab:
#         if b > 0:
#             ile += 1
#     print(ile)
#     if ile > maks:
#         maks = ile
#         maks_s = x
#
# print(maks_s, maks)

#3


for x in lines:

    czy = 1
    for a in range(len(x)):

        for b in range(len(x)):
            if abs(ord(x[a]) - ord(x[b])) > 10:
                czy = 0

    if czy:
        print(x)


