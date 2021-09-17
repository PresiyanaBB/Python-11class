import copy
l=[]
n=int(input('n = '))
for i in range (1,n+1):
    l.append(i)
print(l)
l2 = [i for i in range(l[0],l[len(l)-1]+1,2)]
if n%2==0:
    p=len(l)-1
else:
    p=len(l)-2
l3 = [i for i in range(l[p],l[0],-2)]
print(l2)
print(l3)
l2.extend(l3)
print(f'kraen list {l2}')
