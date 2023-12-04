kullanici_sayisi = int(input("Lütfen bir sayi girin: "))
for i in range(1, kullanici_sayisi+1):

    if i % 2 == 0:
        print(i, end=" ")

print(" ", end="\n")

kullanici_sayisi = int(input("Lütfen bir sayi girin: "))
sayi = 1

while sayi <= kullanici_sayisi:
    if sayi % 2 == 0:
        print(sayi, end=" ")
    sayi +=1