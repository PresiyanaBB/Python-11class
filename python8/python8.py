s = input()
m = input()
for i in range(ord('а'),ord('я') + 1):
    m+=chr(i)
print(m)
l = [c for c in s if(c in m)]
print(l)
s=set(l)
l = list(s)
print(s)
if l==m:
    print('Yes')
else:
    print('No')