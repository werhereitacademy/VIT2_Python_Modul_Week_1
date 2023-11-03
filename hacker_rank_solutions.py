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
