import copy
l=[]
n=int(input('n = '))
for i in range (1,n+1):
    l.append(i)
print(l)
l2 = copy.copy(l)
for i in range (0,len(l2)-1,2):
    l2[i],l2[i+1]=l2[i+1],l2[i]
print(l2)