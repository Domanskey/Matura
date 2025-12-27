lines = open("napisy.txt", "r").read().split()
# lines = open("przyklad.txt", "r").read().split()
# print(lines)

#1

# ile = 0
#
# for x in lines:
#     for a in x:
#         if a == '0' or ( a <='9' and a >= '1'):
#             ile += 1
#
# print(ile)

#2

# i = 0
# j = 20
#
# res = ""
#
# while j <= 1000:
#     res += lines[j - 1][i]
#     # print(j)
#
#     i += 1
#     j += 20
#
# print(res)

#3

# res = ""
#
# for x in lines:
#     slowo = x
#
#     slowo1 = slowo + slowo[0]
#     # print(slowo, slowo1)
#
#     if slowo1 == slowo1[::-1]:
#         res += slowo1[25]
#         continue
#
#     slowo2 = slowo[-1] + slowo
#
#     if slowo2 == slowo2[::-1]:
#         res += slowo2[25]
#         continue
#
# print(res)

#4

# wynik = ""
# for x in lines:
#
#     cyfry = []
#     para = ""
#     i = 0
#     for a in x:
#         if a == '0' or ( a <='9' and a >= '1'):
#             para += a
#             i += 1
#         if i == 2:
#             i = 0
#             if para >= "65" and para <= "90":
#                 cyfry.append(para)
#             para = ""
#
#     res = ""
#     for j in cyfry:
#         litera = chr(int(j))
#         res += litera
#     wynik += res
#     # print(cyfry)
#     # print(res)
#
# ile_x = 0
# ostat = ""
# for c in wynik:
#     ostat += c
#     if c == "X":
#         ile_x += 1
#     if ile_x == 3:
#         break
#
# print(ostat)


def alg1(n):
    dl = 0
    i = n
    while n > 0:
        if i * i <= n:
            print(i)
            n = n - (i * i)
            dl = dl + 1
        else:
            i = i - 1
    print()
    return dl

def alg2(n):
    s = 0
    kw = 1
    while kw * kw < n:
        kw = kw + 1
    if kw * kw > n:
        kw = kw - 1

    s = n - (kw * kw)
    dl = 1
    print(s)
    while s > 0:
        print(s, kw)
        if kw * kw <= s:
            # print(kw)
            s = s - (kw * kw)
            dl = dl + 1
        else:
            kw = kw - 1


    return dl

x = 12
print(alg2(x))


