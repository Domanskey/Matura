import math
lines = open("liczby.txt", "r").read().split()
lines2 = open("pierwsze.txt", "r").read().split()

# lines = open("liczby_przyklad.txt", "r").read().split()
# lines2 = open("pierwsze_przyklad.txt", "r").read().split()

def pierwsza(x):
    x = int(x)
    if x < 2:
        return False
    if x == 2:
        return True
    for a in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % a == 0:
            return False
    return True

#1

# for x in lines:
#     x = int(x)
#     if x >= 100 and x <= 5000:
#         if pierwsza(x):
#             print(x)

#2

# for x in lines2:
#     if pierwsza(x):
#         if pierwsza(x[::-1]):
#             print(x)

#3

def waga(x):
    suma = 0
    while len(x) > 1:
        for a in x:
            suma += int(a)
        x = str(suma)
        suma = 0
    return int(x)

# print(waga("1109"))

ile = 0
for x in lines2:
    if waga(x) == 1:
        ile +=1

print(ile)



