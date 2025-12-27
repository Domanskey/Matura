lines = open("liczby.txt", "r").read().split()
# lines = open("przyklad.txt", "r").read().split()

# print(lines)

#1

# trojki = []
#
# i = 1
# for x in range(100):
#     trojki.append(i)
#     i *= 3
#
# # print(trojki)
#
#
# ile = 0
# for x in lines:
#     x = int(x)
#
#     if x in trojki:
#         ile += 1
#
# print(ile)

#2

# for x in lines:
#     suma_silni = 0
#
#     for a in x:
#         a = int(a)
#         if a == 0:
#             suma_silni += 1
#             continue
#         sil = 1
#         for b in range(1, a + 1):
#             sil *= b
#         suma_silni += sil
#
#     if suma_silni == int(x):
#         print(x)


#3

def nwd(a, b):
    a = int(a)
    b = int(b)
    res = 0
    for x in range(1, min(a,b) + 1):
        if a%x==0 and b%x==0:
            res = x

    return res

maks = 0
m_n = 0
m_p = 0

for x in range(len(lines) - 1):
    n = nwd(int(lines[x]), int(lines[x + 1]))
    dl = 0
    nnn = 0
    if n > 1:

        for a in range(x + 1, len(lines)):
            nk = nwd(n, int(lines[a]))
            if nk > 1:
                n = nk
            else:
                dl = a - x
                break
    if dl > maks:
        maks = dl
        m_p = lines[x]
        m_n = n




print(m_p, maks, m_n)









