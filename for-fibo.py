#Fibonacci sayıları
#0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21
sayı=int(input("Fibonacci sayı adedi girin:"))
sayı1=0
sayı2=1
print(sayı1)
print(sayı2)
for i in range (sayı-2):
    sayı3=sayı1+sayı2
    print(sayı3)
    sayı1=sayı2
    sayı2=sayı3