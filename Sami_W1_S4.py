kilo = int(input("Lütfen kilonuzu girin: "))
boy = float(input("Lütfen boyunuzu girin: "))


#Vücut_kitle_indeksi = v_k_i
v_k_i = kilo / (boy**2)

if v_k_i < 18.5:
    print("İdeal kilonun altında")

if 24.9 > v_k_i > 18.5 :
    print("İdeal kiloda")

if 29.9 > v_k_i >= 25:
    print("İdeal kilonun üstünde")

if 39.9 > v_k_i >= 30:
    print("Obez")

if v_k_i >= 40:
    print("Morbid Obez")