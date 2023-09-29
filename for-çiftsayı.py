"""Soru 1: Kullanıcıdan bir sayı girişi alarak, 1'den kullanıcının
girdiği sayıya kadar olan tüm çift sayıları ekrana yazdıran
bir döngü nasıl oluşturulur? Bunu once 'for' ile sonra 'while' donguleri ile yapiniz"""

user_input=int(input("Lütfen bir sayı giriniz:"))
for i in range(1,user_input):
    if i%2==1:
        continue
    print(i, "çift sayıdır.")

