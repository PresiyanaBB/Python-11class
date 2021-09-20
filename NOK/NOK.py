a,b=map(int, input().split());
if(a>b):
    x=a;
else:
    x=b;
while x<=a*b:
   if(x%a==0 and x%b==0):
      print(x);
      break
   else:
       x=x+1