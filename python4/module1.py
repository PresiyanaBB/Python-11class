def Printer (k):
    for  i in range (k,2*k):
        print(f'{i} ',end='')
n=int(input())
for i in range(1,n+1):
    Printer(i)
    print()
