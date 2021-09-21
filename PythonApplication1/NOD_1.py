def fun(a,b):
    if( a==0 or b==0 ):
        return 0
    else:
        a=a%b
        b=a
        while(a != 0 or b != 0 ):
            return (a)
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if( fun(a,b) == fun(c,d)):
    print ("yes")
else:
    print ("no")
