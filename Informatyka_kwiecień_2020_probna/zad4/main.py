lines = open("dane4.txt", "r").read().split()

print(lines)

#1

# min_n = float("inf")
# max_n = float("-inf")
# for x in range(len(lines) - 1):
#     diff = abs(int(lines[x]) - int(lines[x + 1]))
#
#     max_n = max(diff, max_n)
#     min_n = min(diff, min_n)
#
# print(min_n, max_n)

#2
# maks = 0
# pocz = 0
# kon = 0
# # lines = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]
# for a in range(len(lines) - 1):
#
#     diff = abs(int(lines[a]) - int(lines[a + 1]))
#     ile = 1
#     for b in range(a, len(lines) - 1):
#         d = abs(int(lines[b]) - int(lines[b + 1]))
#
#         if d == diff:
#             ile += 1
#             if ile > maks:
#                 maks = ile
#                 pocz = lines[a]
#                 kon = lines[b + 1]
#         else:
#             break
#
# print(maks, pocz, kon)



#3

# hashmap = {}
#
# for x in range(len(lines) - 1):
#     diff = abs(int(lines[x]) - int(lines[x + 1]))
#
#     hashmap[diff] = hashmap.get(diff, 0) + 1
#
# maks = 0
#
# for x in hashmap.values():
#     if x > maks:
#         maks = x
# print(maks)
#
# for a in hashmap.keys():
#     if hashmap[a] == maks:
#         print(a)


