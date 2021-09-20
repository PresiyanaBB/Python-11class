n=int(input())
def fun(a):
    count = 0
    while(a>0):
        count=count+1
        a=a//10
    return count
for i in range (n):
    a=int(input("a="))
    print(fun(a))
    print()
