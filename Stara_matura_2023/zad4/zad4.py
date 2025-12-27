lines = open("slowa.txt" , "r").read().split()
# lines = open("przyklad.txt" , "r").read().split()

#1


# for x in lines:
#     if x.count('w') == x.count('k'):
#         print(x)


#2
    #wakacje w:1 a:2 k:1 c:1 j:1 e:1

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
#     while w > 0 and a > 1 and k > 0 and c > 0 and j > 0 and e > 0:
#         ile += 1
#         w -= 1
#         a -= 2
#         k -= 1
#         c -= 1
#         j -= 1
#         e -= 1
#
#     print(ile, end=' ')

#3

for x in lines:
    length = 0
    word = ""
    for a in x:
        if a == 'w':
            if word == "":
                word += a
        elif a == 'a':
            if word == "w" or word == "wak":
                word += a
        elif a == 'k':
            if word == "wa":
                word += a
        elif a== 'c':
            if word == "waka":
                word += a
        elif a== 'j':
            if word == "wakac":
                word += a
        elif a == 'e':
            if word == "wakacj":
                word += a
                # print(word)
                length += 7
                word = ""
    print(len(x) - length, end = " ")