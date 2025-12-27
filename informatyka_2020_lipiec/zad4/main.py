lines = open("identyfikator.txt", "r").read().split()
# lines = open("identyfikator_przyklad.txt", "r").read().split()

# 1

# print(lines)
#
# maks = 0
#
# for x in lines:
#         s = x[:3:]
#         num = x[3::]
#         res = 0
#         for a in num:
#             res += int(a)
#         if res > maks:
#             maks = res
#
# for x in lines:
#     s = x[:3:]
#     num = x[3::]
#     res = 0
#     for a in num:
#         res += int(a)
#     if res == maks:
#         print(x)


# 2

# for x in lines:
#         s = x[:3:]
#         num = x[3::]
#         if s == s[::-1] or num == num[::-1]:
#             print(x)

# 3

hashmap = {}

ile = 10
for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    hashmap[x] = ile
    ile += 1

print(hashmap)
print(lines)
for x in lines:
    s = x[:3:]
    control = int(x[3])
    num = x[4::]
    first = [7, 3, 1]
    sec = [7, 3, 1, 7, 3]
    res = 0
    for a in range(3):
        res += hashmap[s[a]] * first[a]

    for a in range(5):
        res += int(num[a]) * sec[a]

    res = res % 10
    # print(res, control)
    if res != control:
        print(x)

