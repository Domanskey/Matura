lines = open("bin.txt", 'r').read().split()
# lines = open("bin_przyklad.txt", 'r').read().split()


#2
# res = 0
#
# for x in lines:
#
#     pop = "5"
#     ile = 0
#     for a in x:
#         if a != pop:
#             ile += 1
#
#         pop = a
#
#     if ile <= 2:
#         res += 1
#
# print(res)

#3

# maks = 0
# maks_b = 0
#
# for x in lines:
#     liczba = int(x, 2)
#     if liczba > maks:
#         maks = liczba
#         maks_b = x
#
# print(maks_b)

#5

for x in lines:
    liczba = int(x, 2)

    pol = liczba // 2

    pol_b = bin(pol).lstrip("0b")
    pol_b = "0" + pol_b
    # print(x, pol_b)

    res = ""

    for a in range(len(x)):
        if x[a] != pol_b[a]:
            res += "1"
        else:
            res += "0"

    print(res)




