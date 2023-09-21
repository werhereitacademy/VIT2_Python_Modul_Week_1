#Soru1_a for döngüsü
x=int(input("Bir sayı giriniz"))
for i in range(1, x):
    if i % 2 == 0:
        print(i)

#Soru1_b while döngüsü
x=int(input("Bir sayı giriniz"))
i=1
while (i<=x):
    if i % 2 == 0:
        print(i)
    i=i+1

#Soru2_a for döngüsü
a = 0
b = 1
c = 0
n=1000;
print("Bir değer giriniz : ", end="")
x = int(input())
fibo=[0,1]
c = a+b
for i in range(1,n-1):
    if(c>x):
        break
    fibo.append(c)
    a = b
    b = c
    c = a+b
for i in fibo:
    print(i, end=" ")

#Soru2_b while döngüsü
a = 0
b = 1
c = 0
n=1000;
print("Bir değer giriniz : ", end="")
x = int(input())
#print("\nFibonacci Serisi :", a, b, end=" ")
fibo=[0,1]
c = a+b
while(True):
    if(c>x):
        break
    fibo.append(c)
    a = b
    b = c
    c = a+b
i=0   
while(i<len(fibo)):
    print(fibo[i], end=" ")
    i=i+1

#Soru3
word = input("kelime girin: ")
start = len(word)-1
i=0
word2=''
for index in word:
  word2 = word2 + word[start]
  start=start-1

print(word2)
if word == word2:
    print("  Palindromdur")
else:
    print("  Palindrom değildir")

#Soru4
kilo=float(input("Kilonuzu girin : "))
boy=float(input("Boyunuzu girin : "))
vki=kilo/(boy*boy)
print(vki)
if (vki<25):
    print("zayıfsınız")
elif (vki>=25 and vki<30):
    print("Normal kilodasınız")
elif (vki>=30 and vki<40):
    print("Kilolusunuz")
else:
    print("Asırı kilosunuz")


