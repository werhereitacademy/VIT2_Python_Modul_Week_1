1- https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a+b)
print(a-b)
print(a*b)

2- https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    given_list = [2,3,6,6,5]
    unique_scores = sorted(set(arr))
if len(unique_scores)>1:
    runner_up_score = unique_scores[-2]
    print(runner_up_score)
    
else:
    print("There is no runner up score")

3- https://www.hackerrank.com/challenges/python-print/problem

n = int(input())

output = ""

for i in range(1, n+1):
    output += str(i)

print(output)

4- https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())

ogrenci_notlari = {}

for _ in range(n):
    isim, *notlar = input().split()
    ogrenci_notlari[isim] = list(map(float, notlar))

aranan_isim = input()

ortalama_not = sum(ogrenci_notlari[aranan_isim]) / len(ogrenci_notlari[aranan_isim])

print("{:.2f}".format(ortalama_not))




