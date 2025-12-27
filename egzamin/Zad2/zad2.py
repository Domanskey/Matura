lines = open("bin.txt", "r").read().split('\n')
# lines = open("bin_przyklad.txt", "r").read().split('\n')

#2

# print(lines)
# ile = 0
#
# for a in lines:
#     pop = '2'
#     bloki = 0
#     for b in a:
#         if b != pop:
#             bloki += 1
#         pop = b
#     if bloki <= 2:
#         ile += 1
#
#
# print(ile)

#3

# for a in lines:
#     maks = 0
#     for b in lines:
#
#         b = int(b, 2)
#         if b> maks:
#             maks = b
#         # print(b)
#
# print(bin(maks))

#5

for a in lines:


    pierwsza = str(a)

    druga = "0" + str(a)
    # druga.pop()
    trzecia =""
    for b in range(len(a)):
        if pierwsza[b] != druga[b]:
            trzecia += '1'
        else:
            trzecia += '0'

    print(trzecia)




