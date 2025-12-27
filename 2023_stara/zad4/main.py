lines = open("slowa.txt").read().split()
# lines = open("przyklad.txt").read().split()
print(lines)

#1

# for x in lines:
#
#     w = x.count('w')
#     k = x.count('k')
#
#     if w == k:
#         print(x)


#2


# for x in lines:
#     w = x.count('w')
#     a = x.count('a')
#     k = x.count('k')
#     c = x.count('c')
#     j = x.count('j')
#     e = x.count('e')
#
#     ile = 0
#
#     while w >= 1 and a >= 2 and k >= 1 and c >= 1 and j >= 1 and e >= 1:
#         ile += 1
#         w -= 1
#         a -= 2
#         k -= 1
#         c -= 1
#         j -= 1
#         e -= 1
#
#     print(ile, end=" ")

#3

for x in lines:
    slowo = ""
    ile = 0

    for a in x:

        if slowo == "" and a == "w":
            slowo += a
        elif slowo == "w" and a == "a":
            slowo += a
        elif slowo == "wa" and a == "k":
            slowo += a
        elif slowo == "wak" and a == "a":
            slowo += a
        elif slowo == "waka" and a == "c":
            slowo += a
        elif slowo == "wakac" and a == "j":
            slowo += a
        elif slowo == "wakacj" and a == "e":
            slowo += a
            slowo = ""
        else:
            ile += 1

    if slowo != "":
        ile += len(slowo)

    print(ile, end=" ")