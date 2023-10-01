#Soru 1:
#For Döngüsü
sayı = int(input("Bir Sayı Giriniz:"))
for k in range(1,sayı+1):
    if k % 2 == 0:
        print(k,"Çift Sayıdır.")

#while Döngüsü
yeni_sayı = int(input("Bir Sayı Giriniz:"))

s = 1
while (s<=yeni_sayı):
    if s % 2 == 0:
        print(s,"Bir Çift Sayıdır.")
    s = s+1


#Soru 2:
#For Döngüsü
a = 0
b = 1
fibonacci = [a,b]
sınır = int(input("Bir Değer Giriniz:"))
c = a+b
for i in range(sınır-2):
    c = a + b
    if c >= sınır:
        break
    a = b
    b = c
    fibonacci.append(c)
print(fibonacci)

#while Döngüsü
sınır = int(input("Bir Değer Giriniz:"))
fibo_list =[]
def fibo():
    a,b = 0,1
    while a<sınır:
        fibo_list.append(a)#bu listeli hali
        a,b = b,(a+b)
fibo()
print(fibo_list)

#Soru 3:
palindrom = True
print("Çıkmak için q'ya basınız.")
while palindrom:
    metin = input("Kelime Giriniz:").lower()
    ters = metin[::-1]
    if metin == "q":
        palindrom = False
    else:
        if metin == ters:
            print(metin,"Palindrom'dur.")
        else:
            print(metin,"Palindrom Değildir.")


Soru 4:
print("Kilo İndeksi Hesaplama")

kilo = int(input("Lütfen Kilonuzu Kg Olarak Giriniz:"))
boy = float(input("Lütfen Boyunuzu Metre Olarak Giriniz:"))

bki = kilo / (boy*boy)
print(bki)
if (bki <= 25):
    print("Sonuç=",bki,"Zayıf!")
elif (bki >= 25 and bki <= 30): 
    print("Sonuç=",bki,"Normal")
elif (bki >= 30 and bki <= 40):
    print("Sonuç=",bki,"Kilolu!")
else:
    print("Sonuç=",bki,"Aşırı Kilolu!")




