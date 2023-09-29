 Soru 1: Kullanıcıdan bir sayı girişi alarak, 1'den kullanıcının girdiği sayıya kadar olan tüm çift sayıları ekrana yazdıran bir döngü nasıl oluşturulur? Bunu once 'for' ile sonra 'while' donguleri ile yapiniz

  # for dongusu ile cift sayilar
sayi = int(input("lutfen bir sayi giriniz: "))
for i in range (2, sayi + 1, 2):
    print (i)
# while dongusu ile cift sayilar:

sayi = int(input("lutfen bir sayi giriniz:"))
i = 2
while i <= sayi:
      print (i)
      i += 2


 Soru 2: Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar olan sayıları içeren bir liste olarak döndüren bir döngü nasıl oluşturulur? Bunu once 'for' ile sonra 'while' donguleri ile yapiniz.

fibonacci_sinir = int(input("Fibonacci dizisi icin bir sinir giriniz:"))

fibonacci = [0,1]

for i in range (2, fibonacci_sinir):
    son_sayi = fibonacci[-1]
    bironceki_sayi = fibonacci[-2]
    yeni_sayi = son_sayi + bironceki_sayi
    if yeni_sayi <= fibonacci_sinir:
       fibonacci.append(yeni_sayi)
    else:
        break
print (fibonacci)


Soru 3: Kullanıcıdan bir kelime girişi alan ve bu kelimenin palindrom (tersten okunduğunda aynı olan) olup olmadığını kontrol eden bir döngü ve koşullu ifade kombinasyonu nasıl oluşturulur?

palindrom = input ("lutfen bir kelime giriniz:")

tersten = palindrom[::-1]

if palindrom == tersten:
    print ("Evet bu bir palindrom")
else:
    print ("Hayir bu bir palindrom degil")



- Soru 4: Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.(kilo indeks hesabı için internete bakabilirsiniz)
Bunun için kullanıcıdan kilo ve boy ölçülerini isteyiniz. Kilo indeksi 25’in altında ise zayıf, 25-30  arasında ise normal, 30-40`dan büyük ise kilolu, 40`tan büyük ise aşırı kilolu sonuçlarına varsın.

kilo = int(input("Kac kilosunuz:"))
boy = int(input("boyunuzu giriniz:"))

kilo_indeksi = kilo / (boy*boy)
if kilo_indeksi < 25:
    print ("Biraz kiloya ihtiyaciniz var.")
elif kilo_indeksi >= 25:
    print ("Boy kilo oraniniz ideal")
elif kilo_indeksi >= 30:
    print ("Fazladan kilonuz var.")
elif kilo_indeksi >= 40:
    print ("Asiri kilolu grubundasiniz. Sagliginiz icin kilo verin.")


