lines = open("mecz.txt", "r").read().split()
# lines = open("mecz_przyklad.txt", "r").read().split()
lines = lines[0]
print(lines)


#1

# ile = 0
# for x in range(len(lines) - 1):
#     if lines[x] != lines[x + 1]:
#         ile += 1
#
# print(ile)

#2

# a = 0
# b = 0
# for x in lines:
#     if x == 'B':
#         b += 1
#     if x == 'A':
#         a += 1
#
#     if max(a,b) >= 1000 and max(a,b) - min(a,b) >= 3:
#         break
#
# if a > b:
#     print('A', f"{a}:{b}")
# else:
#     print('B', f"{a}:{b}")

#3

# lines = "BBBBBBBBBBAABBAAAAAAAAAAABA"

# ile = 0
# pop = 0
# passa = 1
# pass_max = 0
# maks_litera = 0
#
# for x in lines:
#     if x != pop:
#         if passa >= 10:
#             ile += 1
#         passa = 1
#     else:
#         passa += 1
#         if passa > pass_max:
#             pass_max = passa
#             maks_litera = x
#     pop = x
#
# print(ile, maks_litera, pass_max)

