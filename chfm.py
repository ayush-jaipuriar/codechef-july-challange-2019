#Test Cases
from statistics import mean

t = int(input())

for i in range(t):
    
    n = int(input())
    a = list(map(int,input().split()))

    avg = mean(a)

    if avg in a:
        print(a.index(avg) + 1)

    else:
        print('Impossible')