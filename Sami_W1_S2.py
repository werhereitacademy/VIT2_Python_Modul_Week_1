a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

liste=[]
a=0
b=1
for i in range(10):
    top = a + b
    a = b
    b= top
    liste.append(top)
print(liste, end=" ")


a, b = 0, 1
say = 0
while say <10:
    print(a, end=" ")
    a, b = b, a + b
    say +=1

#en basa bos liste tanimla ve liste.append(toplam)