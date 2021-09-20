a=int(input());
b = (365-a)*63 + a*127;
if(b>30000):
    print("will run away\n",int((b-30000)/60),"hours and ",(b-30000)%60," minutes"," too much");
else:
    print("sleeps well\n",int((30000-b)/60),"hours and ",(30000-b)%60," minutes"," left");
c=int(input());

