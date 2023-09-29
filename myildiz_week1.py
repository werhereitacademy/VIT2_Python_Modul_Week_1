soru1:Kullanıcıdan bir sayı girişi alarak, 1'den kullanıcının girdiği sayıya kadar olan tüm çift sayıları ekrana yazdıran bir döngü nasıl oluşturulur? Bunu once 'for' ile sonra 'while' donguleri ile yapiniz

user_input=int(input("Lütfen bir sayı giriniz:"))
for i in range(1,user_input):
    if i%2==1:
        continue
    print(i, "çift sayıdır.")

user_input=int(input("Lütfen bir sayı giriniz:"))
x=2
while x<user_input:
        print(x)
        x+=2
  
  Soru 2: Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar olan sayıları içeren bir liste olarak döndüren bir döngü nasıl oluşturulur? Bunu once 'for' ile sonra 'while' donguleri ile yapiniz.

  #Fibonacci sayıları
#0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21
sayı=int(input("Fibonacci sayı adedi girin:"))
sayı1=0
sayı2=1
liste=[]
for i in range (sayı):
    sayı3=sayı1+sayı2
    sayı1=sayı2
    sayı2=sayı3
    liste.append(sayı3)
print(liste)

#Fibonacci sayı dizisi
#0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21
hedef_sayı=int(input("Lütfen bir sayı giriniz:"))
sayı1=0
sayı2=1
liste=[]
while sayı1+sayı2<=hedef_sayı:
    sayı3=sayı1+sayı2
    sayı1=sayı2
    sayı2=sayı3
    liste.append(sayı3)
print(liste)

Soru 3: Kullanıcıdan bir kelime girişi alan ve bu kelimenin palindrom (tersten okunduğunda aynı olan) olup olmadığını kontrol eden bir döngü ve koşullu ifade kombinasyonu nasıl oluşturulur?
while True:
    sözcük1=input("Sözcük1:")
    sözcük2=sözcük1[::-1]
    print("Girilen sözcük1 in tersi:", sözcük2)
    if sözcük1==sözcük2:
        print("Girilen sözcük, palindromdur.")
        break
    else:
        print("Girilen sözcük palindrom değildir. Tekrar deneyiniz!")
    #Vücut kitle endeksi(vke)=Kilo(kg)/Boy(m)*Boy(m)
kilo=float(input("Kullanıcının kilosu:"))
boy=float(input("Kullanıcının boyu:"))
vke=kilo/(boy**2)
print("Vücut Kitle Endeksi:",vke)
if vke>40:
    print("Kişi aşırı kilolu")
elif vke>=30:
    print("Kişi kilolu")
elif vke>=25:
    print("Kişi normal kilolu")
else:
    print("Kişi zayıf") 4: Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.(kilo indeks hesabı için internete bakabilirsiniz) Bunun için kullanıcıdan kilo ve boy ölçülerini isteyiniz. Kilo indeksi 25’in altında ise zayıf, 25-30 arasında ise normal, 30-40dan büyük ise kilolu, 40tan büyük ise aşırı kilolu sonuçlarına varsın.
    
