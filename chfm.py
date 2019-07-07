
from statistics import mean

for i in range(int(input())):
    
    n = int(input())
    a = list(map(int,input().split()))

    avg = mean(a)

    if avg in a:
        print(a.index(avg) + 1)

    else:
        print('Impossible')
