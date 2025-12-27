lines = open("pi.txt", "r").read().split()
# lines = open("pi_przyklad.txt", "r").read().split()

print(lines)
#1

# ile = 0
#
# for b in range(len(lines) - 1):
#     liczba = lines[b] + lines[b+1]
#     liczba = int(liczba)
#
#     # print(liczba)
#
#     if liczba>90:
#         ile += 1
#
# print(ile)

#2
# mozliwosci = []
# wyniki = [0]*105
# for a in range(0, 10):
#     for c in range(0,10):
#         l = str(a) + str(c)
#         mozliwosci.append(l)
#
# # print(mozliwosci)
#
#
# for b in range(len(lines) - 1):
#     liczba = lines[b] + lines[b+1]
#     print(liczba)
#     wyniki[mozliwosci.index(liczba)] += 1
#
#
# maks = 0
# kl = 0
# for d in range(100):
#     if wyniki[d] > maks:
#         maks = wyniki[d]
#         kl = d
#     elif wyniki[d] == maks:
#         if d<kl:
#             kl = d
#
# min = float("inf")
# minkl = 0
# for e in range(100):
#     if wyniki[e] < min:
#         min = wyniki[e]
#         minkl = e
#     elif wyniki[e] == min:
#         if e<minkl:
#             minkl=e
#
# print(kl,maks,"  ", minkl, min)

#3
ciagi = set()
ile = 0
for b in range(len(lines)-6+1):
    rosnie = True
    maleje = True
    liczba_pop = lines[b]
    for c in range(1, 6):
        liczba_ob = lines[b+ c]

        if rosnie and liczba_ob <= liczba_pop:
            rosnie = False
        elif not rosnie and maleje and liczba_ob>=liczba_pop:
            maleje = False
            break
        liczba_pop = liczba_ob

    if not rosnie and maleje:
        ciagi.add(str(lines[b:b+5:1]))
        print(lines[b:b+c+1])

print(len(ciagi))

#4

pozycja = 0
maks = 0
ciag = 0
for b in range(len(lines)):
    rosnie = True
    maleje = True
    liczba_pop = lines[b]
    for c in range(1, len(lines) - b):
        liczba_ob = lines[b+c]

        if rosnie and liczba_ob<=liczba_pop:
            rosnie = False
        elif not rosnie and maleje and liczba_ob>=liczba_pop:
            maleje = False
            break
        liczba_pop = liczba_ob

        if c+1>maks:
            maks = c+1
            pozycja = b + 1
            ciag = lines[b:b+c+1]

print(pozycja, maks, ciag)
