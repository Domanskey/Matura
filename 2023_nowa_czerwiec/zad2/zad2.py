
def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2

    while i < n and j < n:
        if s[i] == s[j]:
            i = i + 1
            j = j + 1
        else:
            if s[i] < s[j]:
                return "TAK"
            else:
                return "NIE"

    if j < n:
        return "TAK"
    else:
        return "NIE"



lines = open("sufiks_4.txt" , "r").read().split('\n')
lines = open("slowa4.txt" , "r").read().split('\n')
# lines = ['5 banan']

for x in lines:
    x = x.split()
    n = int(x[0])
    s = x[1]

    tab = [x for x in range(n)]
    # print(len(tab))
    for i in range(n):

        for j in range(n - 1):
            if czy_mniejszy(n, s, tab[j], tab[j + 1]) == "NIE":
                # print('yolo')
                yolo = tab[j + 1]
                tab[j + 1] = tab[j]
                tab[j] = yolo

    print(s[tab[0]:])




# print(yolo)