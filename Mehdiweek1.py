#1.soru
sayi = (int(input("Lutfen 1 den buyuk bir sayi giriniz:")))
for n in range(2, sayi, 2):
    print(n)
x = 2
while x < sayi:
    print(x)
    x += 2
  
  
  #2.soru
  esas_sayi = int(input("Lutfen bir sayi giriniz:"))

ilk_sayi = 0
next_sayi = 1

while ilk_sayi + next_sayi <= esas_sayi :
    hesap = ilk_sayi + next_sayi
    ilk_sayi = next_sayi
    next_sayi = hesap
    print(next_sayi, end = " ")

#3.soru
kelime = str(input("Lutfen bir kelime giriniz:").lower())
ters_kelime = kelime[::-1]
if kelime == ters_kelime:
    print("Evet bu bir palindrom")
else:
    print("Bu bir palindrom degil")
while ters_kelime == kelime:
    print("Bu bir palindrom")
    break
else:
    print("Su bir palindrom degil")


#4.soru
kilo = float(input("Lutfen kilonuzu giriniz:"))
uzunluk = float(input("Lutfen boyunuzu giriniz(cm):"))
indeks = kilo / (uzunluk/100)**2
print("Vucut Indeksiniz:",int(indeks))
if indeks <= 25:
    print("zayif")
elif indeks >25 and indeks <= 30:
    print("normal")
elif indeks > 30 and indeks <= 40:
    print("Kilolu")
else:
    print("Asiri Kilolu")
