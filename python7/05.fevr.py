from random import randint
def Rand(n):
    l=[]
    for i in range (1,n+1):
        r=randint(20,101)
        l.append(r)
    return l
def Min(s):
    min=s[0]
    for el in s:
        if el<min:
            min=el
    return min

if __name__=='__main__':
    n=int(input('n: '))
    L=Rand(n)
    print(L)   
    print(str(Min(L))+" "+str(max(L)))
