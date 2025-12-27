lines1 = [x.split() for x in open("dane1.txt", "r").read().split('\n')]
lines2 = [x.split() for x in open("dane2.txt", "r").read().split('\n')]

# lines1 = [x.split() for x in open("przyklad1.txt", "r").read().split('\n')]
# lines2 = [x.split() for x in open("przyklad2.txt", "r").read().split('\n')]

# print(lines1)
#1
# ile = 0
# for x in range(len(lines1)):
#
#     a, b = lines1[x][-1], lines2[x][-1]
#
#     if a == b:
#         ile += 1
# print(ile)

#2

# ile = 0
# for x in range(len(lines1)):
#     par1 = 0
#     par2 = 0
#
#     for a in lines1[x]:
#         if int(a) % 2 == 0:
#             par1+=1
#
#     for b in lines2[x]:
#         if int(b) % 2 == 0:
#             par2+=1
#
#     if par1 == 5 and par2 == 5:
#         ile += 1
# print(ile)

#3
# ile = 0
# for x in range(len(lines1)):
#
#     set1 = set(lines1[x])
#     set2 = set(lines2[x])
#
#     if set1 == set2:
#         ile += 1
#         print(x + 1)
# print()
# print(ile)

#4


for x in range(len(lines1)):

    pierwszy = [int(a) for a in lines1[x] ]
    drugi = [int(b) for b in lines2[x]]

    res = []

    i = 0
    j = 0
    while i < len(pierwszy) and j < len(drugi):
        if pierwszy[i] <= drugi[j]:
            res.append(pierwszy[i])
            i += 1
        else:
            res.append(drugi[j])
            j += 1

    while j < len(drugi):
        res.append(drugi[j])
        j += 1
    while i < len(pierwszy):
        res.append(pierwszy[i])
        i += 1

    print(res)

