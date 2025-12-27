print('yolo')

arr = ["9", "8","7","6","5","4","3","2","1","0", "10"]
arr.sort()
print(arr)


blok = 0
pop = -1
liczba = 245
while liczba > 0:
    cyfra = liczba % 2
    print(cyfra)
    if cyfra != pop:
        blok += 1
    liczba = liczba // 2
    pop = cyfra

print()
print(blok)
