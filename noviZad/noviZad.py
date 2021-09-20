a = int(input("a = "))
def sum(a):
    if(a==0):
        return 0
    return a + sum(a-1)
print(a)