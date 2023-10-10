kelime = input("Lütfen bir kelime girin: ").lower()

if kelime == kelime[::-1]:
    print("Yazdiginiz", kelime, "bir palindromdur.")

else:
    print("Yazdiginiz", kelime, "bir palindrom DEGILDIR.")