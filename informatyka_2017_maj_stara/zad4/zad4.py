lines = open("binarne.txt", "r").read().split()

# print(lines)
#1
# ile = 0
# maks = 0
# jaki_maks = 0
# for x in lines:
#     l = len(x)
#     if l % 2 == 0:
#
#         if x[:l // 2] == x[l//2:]:
#             ile += 1
#             if l > maks:
#                 maks = l
#                 jaki_maks = x
#
# print(ile, maks, jaki_maks)

#2
# ile = 0
# min_dl = float("inf")
# for x in lines:
#     l = len(x)
#     pop = 0
#     i = 4
#
#     blad = 0
#     while i <= l:
#         segment = x[pop:i]
#
#         liczba = int(segment, 2)
#         # print(liczba)
#         if liczba > 9:
#             blad = 1
#             break
#
#         i += 4
#         pop += 4
#     if blad == 1:
#         ile += 1
#         if l < min_dl:
#             min_dl = l
#
# print(ile, min_dl)


#3

# maks = 0
# maks_bin = 0
#
#
# for x in lines:
#     liczba = int(x, 2)
#
#     if liczba > 65535:
#         continue
#
#     if liczba > maks:
#         maks = liczba
#         maks_bin = x
#
# print(maks, maks_bin)

