import math
n=int(input())
for i in range (n):
    a,b=map(int,input().split())
    nod=math.gcd(a,b)
    print(f'{a//nod}/{b//nod}')
    print()
