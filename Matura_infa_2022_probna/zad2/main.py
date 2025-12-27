lines = open("pary.txt", "r").read().split('\n')

def rysuj(x, N, hashmap):
    if 2*x <= N:
        hashmap.append(2*x)
        rysuj(2*x,N,hashmap)
    if 2*x + 1<= N:
        hashmap.append(2 * x + 1)
        rysuj(2*x + 1,N,hashmap)

# rysuj(1)

# lines = ["1 5", "4 15"]
for x in lines:
    y = x.split()
    first = int(y[0])
    second = int(y[1])


    hashmap = []
    rysuj(first,second, hashmap)
    # print(hashmap)
    if second in hashmap:
        print(x)