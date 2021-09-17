def Nums(n):
    l=[]
    for i in range(n):
        l.append(i)
    return l
def Chetni(list):
    chetno = []
    for el in list:
        if(el//2==0):
            chetno.append(el)
    return chetno

if '_name_' == '_main_':
    a = int(input())
    print(Nums(list(a)))