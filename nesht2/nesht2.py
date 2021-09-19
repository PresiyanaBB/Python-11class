def fun(a):
    count = 0
    while(a>0):
        count=count+a%10
        a=a//10
    return count
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=int(input("d= "))
if( fun(a)+fun(b) == fun(c)+fun(d)):
    print ("yes")
else:
    print ("no")
