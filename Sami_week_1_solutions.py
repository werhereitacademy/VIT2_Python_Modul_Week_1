#soru1_cevabi

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


  
#soru2_cevabi

a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

a, b = 0, 1
say = 0
while say <=10:
    print(a, end=" ")
    a, b = b, a + b
    say +=1


#soru3_cevabi

kelime = input("Lütfen bir kelime girin: ")
if kelime == kelime[::-1]:
    print("Yazdiginiz", kelime, "bir palindromdur.")
else:
    print("Yazdiginiz", kelime, "bir palindrom DEGILDIR.")


#soru4_cevabi

kilo = int(input("Lütfen kilonuzu girin: "))
boy = float(input("Lütfen boyunuzu girin: "))
#Vücut_kitle_indeksi = v_k_i
v_k_i = kilo / (boy**2)
if v_k_i < 18.5:
    print("İdeal kilonun altında")
if 24.9 > v_k_i > 18.5 :
    print("İdeal kiloda")
if 29.9 > v_k_i >= 25:
    print("İdeal kilonun üstünde")
if 39.9 > v_k_i >= 30:
    print("Obez")
if v_k_i >= 40:
    print("Morbid Obez")
