def fun(a):
    count = 0
    while(a>0):
        count=count+1
        a=a//10
    return count
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=int(input("d= "))
print(fun(a)," ",fun(b)," ",fun(c)," ",fun(d));