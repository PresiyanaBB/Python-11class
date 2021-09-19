a=int(input());
b=int(input());
if(a>b):
    x=a;
else:
    x=b;
while x>0:
   if(a%x==0 and b%x==0):
      print(x);
      break
   else:
       x=x-1