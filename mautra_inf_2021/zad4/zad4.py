lines = [x.split() for x in open("instrukcje.txt", "r").read().split('\n')]
# lines = [x.split() for x in open("przyklad.txt", "r").read().split('\n')]
print(lines)


#1

# res = []
#
# for x in lines:
#     ins = x[0]
#     litera = x[1]
#
#     if ins == "DOPISZ":
#         res.append(litera)
#     elif ins == "ZMIEN":
#         res[-1] = litera
#     elif ins == "USUN":
#         res.pop()
#     elif ins == "PRZESUN":
#         for a in range(len(res)):
#             if res[a] == litera:
#                 if res[a] == "Z":
#                     res[a] = "A"
#                 else:
#                     liczba = ord(res[a])
#                     liczba += 1
#                     res[a] = chr(liczba)
#                 break
#
# print(res)
# print("".join(res))

# liczba = ord("A")
# liczba += 1
# print(chr(liczba))

#2
# ile = 0
# pop = 0
# maks = 0
# jaka_maks = 0
#
# for x in lines:
#     ins = x[0]
#     if ins != pop:
#         ile = 1
#     else:
#         ile += 1
#     if ile > maks:
#         maks = ile
#         jaka_maks = ins
#     pop = ins
#
# print(jaka_maks, maks)

#3

# hashmap = {}
#
# for x in lines:
#     ins = x[0]
#     l = x[1]
#
#     if ins == "DOPISZ":
#         hashmap[l] = hashmap.get(l, 0) + 1
#
# maks = 0
# jaka_maks = 0
#
# for key, val in hashmap.items():
#     print(key, val)
#     if val > maks:
#         maks = val
#         jaka_maks = key
#
# print(jaka_maks, maks)

#4





