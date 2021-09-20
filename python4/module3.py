def Printer (k,n):
    s=' '
    print(f'{2*s*(n-k)} ',end='')
    for  i in range (1, k+1):
        print(f'{i} ',end='')
    for i in range (k-1,0,-1):
        print(f'{i} ',end='')
n=int(input())
for i in range(1,n+1):
    Printer(i,n)
    print()
