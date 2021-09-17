class Complex:
    def __init__(self,_re=0,_im=0):
        self.re=_re
        self.im=_im


    def __str__(self):
        if self.im>=0:
            return str(self.re)+"+"+str(self.im)+"i"
        else:
            return str(self.re)+str(self.im)+"i"


    def __add__(self,other):
        if isinstance(other,int) or isinstance(other,float):
            x=Complex(other,0)
        if isinstance(other,Complex):
            re=self.re+other.re
            im=self.im+other.im
        elif isinstance(other,int) or isinstance(other,float):
            re=self.re+x.re
            im=self.im+x.im
        else:
            pass
        return Complex(re,im)


    def __sub__(self,other):
        if isinstance(other,int) or isinstance(other,float):
            x=Complex(other,0)
        if isinstance(other,Complex):
            re=self.re-other.re
            im=self.im-other.im
        elif isinstance(other,int) or isinstance(other,float):
            re=self.re-x.re
            im=self.im-x.im
        else:
            pass
        return Complex(re,im)


    def __mul__(self,other):
        if isinstance(other,Complex):
            re=self.re*other.re-self.im*other.im
            im=self.re*other.im+self.im*other.re
        elif isinstance(other,int) or isinstance(other,float):
            re=self.re*other
            im=self.im*other
        else:
            pass
        return Complex(re,im)


    __rmul__=__mul__
    __radd__=__add__
    __rsub__=__sub__


if __name__=="__main__":
    a=Complex(2,3)
    b=Complex(3,-4)
    c=Complex()
    print()
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')


    print('\nсъбиране')
    print(f'a+b={a+b}')
    print(f'b+a={b+a}')
    print(f'({a})+5={a+5}')
    print(f'5+({a})={5+a}')


    print('изваждане\n')
    print(f'a-b={a-b}')
    print(f'b-a={b-a}')
    print(f'({a})-6={a-6}')
    print(f'6-({a})={6-a}')


    print('умножение\n')
    print(f'a*b={a*b}')
    print(f'b*a={b*a}')
    print(f'({a})*5={a*5}')
    print(f'5*({a})={5*a}')
