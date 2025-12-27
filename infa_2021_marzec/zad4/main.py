lines = [x.split() for x in open("galerie.txt", "r").read().split('\n')]
# lines = [x.split() for x in open("galerie_przyklad.txt", "r").read().split('\n')]

# print(lines)
galerie = []
for x in lines:
    galeria = []
    para = []
    for a in range(len(x)):
        para.append(x[a])
        if a % 2== 1:
            galeria.append(para)
            para = []
    galerie.append(galeria)

print(galerie)
#1

# hashmap = {}
#
# for x in galerie:
#     znak = x[0][0]
#     hashmap[znak] = hashmap.get(znak, 0) + 1
#
# for a in hashmap.keys():
#     print(a, hashmap[a])


#2
# min_g = 0
# min = float("inf")
# max_g = 0
# maks = 0
#
# for x in galerie:
#     znak, miasto = x[0]
#     ile = 0
#     pole =0
#     for a in range(1, 71):
#         z = int(x[a][0])
#         y = int(x[a][1])
#         if z > 0 and y > 0:
#             ile += 1
#             pole += (z * y)
#
#     if pole < min:
#         min = pole
#         min_g = miasto
#
#     if pole > maks:
#         maks = pole
#         max_g = miasto
#
#     print(miasto, pole, ile)
# print()
# print(max_g, maks)
# print(min_g, min)


#3


# min_g = 0
# min = float("inf")
# max_g = 0
# maks = 0
#
# for x in galerie:
#     znak, miasto = x[0]
#     rozne = set()
#     for a in range(1, 71):
#         z = int(x[a][0])
#         y = int(x[a][1])
#         if z > 0 and y > 0:
#             pole = (z * y)
#             rozne.add(pole)
#
#     if len(rozne) < min:
#         min = len(rozne)
#         min_g = miasto
#
#     if len(rozne) > maks:
#         maks = len(rozne)
#         max_g = miasto
#
# print(max_g, maks)
# print(min_g, min)
