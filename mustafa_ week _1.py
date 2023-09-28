### Soru 1 met for ###

n = int(input("Lutfen bir sayi giriniz"))
for n in range(n):
    if n%2 == 0:
        print(n)


#### Soru 1 met while ###

n = int(input("Lutfen bir sayi giriniz  : "))
k = 1
while True:
    k += 1
    if k%2 != 0:
        print(k-1)
    if k == n:
        break


#### Soru 2 met for ###

liste = []
sayi1 = 0
sayi2 = 1
for n in range(20):
    toplam = sayi1 + sayi2
    sayi1 = sayi2
    sayi2 = toplam
    liste.append(sayi2)
    
print(liste)

#### Soru 2 met while ###

liste = []
sayi1 = 0
sayi2 = 1
toplam = 1
while toplam < 100 :
    toplam = sayi1 +sayi2
    sayi1 = sayi2
    sayi2 = toplam
    liste.append(sayi2)
print(liste)


#### Soru 3 ###

n = input("bir kelime giriniz")
metin = n.lower()
liste = []
for karakter in metin:
    liste.append(karakter)
lengthe = len(liste)
sayi = 0
for i in range(lengthe):
   if liste[i] != liste[lengthe - i - 1]:
      sayi += 1
   else:
      sayi = 0
if sayi == 0:
   print("palindromdur")
else:
   print("maalesef degildir")


### Soru 4 ###

ilo = int(input("Lutfen kilonuzu giriniz:"))
boy = int(input("Lutfen boyunuzu cm olarak giriniz:"))
kiloboy_index = kilo/((boy**2)/10000)
if kiloboy_index> 40:
    print("Asiri kilolusunuz")
elif kiloboy_index>30 and kiloboy_index<=40:
    print("Kilolusunuz")
elif kiloboy_index>=25 and kiloboy_index<=30:
    print("Normal")
else:
    print("Zayifsiniz")


###   https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b,end= '\n')
    print(a-b,end= '\n')
    print(a*b,end= '\n')


###   https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

   n = int(input())
    arr = map(int, input().split())
    my_array = list(arr)
print(max([x for x in my_array if x != max(my_array)]))


###    https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    for x in range(n):
        x += 1
        print(x, end="")

    
