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
    print("Kişi zayıf")
