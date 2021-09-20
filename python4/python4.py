def Printer (k):
    for  i in range (1, k+1):
        print(f'{i} ',end='')
n=int(input())
for i in range(1,n+1):
    Printer(i)
    print()