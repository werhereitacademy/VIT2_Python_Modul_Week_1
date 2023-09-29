while True:
    sözcük1=input("Sözcük1:")
    sözcük2=sözcük1[::-1]
    print("Girilen sözcük1 in tersi:", sözcük2)
    if sözcük1==sözcük2:
        print("Girilen sözcük, palindromdur.")
        break
    else:
        print("Girilen sözcük palindrom değildir. Tekrar deneyiniz!")