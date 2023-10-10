if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = list(set(arr))  #girilen rakamlari listeler ve set ile tekrarlari siler
    arr2.sort() #rakamlari kucukten buyuge siralar
    x =arr2[-2]
    print(x)  #2. buyuk rakami yazdirir
