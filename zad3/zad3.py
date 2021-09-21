a = [int(x) for x in input().split()]
b=0
for i in range (len(a)):
    if(i%2==0):
        if(a[i]%2==0):
            b+=1
print(b)