def GiaiPhuongTrinhBac1(a,b):
    """
    Đây là phương trình bậc 1
    :param a: hệ số a
    :param b: hệ số b
    :return: Nghiệm
    """
    if a==0:
        if b==0:
            print (f'{a}x+{b}=0 có vô số nghiệm')
        else:
            print (f'{a}x+{b}=0  vô nghiệm')
    else:
        x=round(-b/a,2)
        print (f'{a}x+{b}=0  có {x} là nghiệm')

a=0
b=0
#GiaiPhuongTrinhBac1(0,0)


def Fibo(n):
    if n<=2:
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)
def pick_Fibo(n):
    fi =Fibo(n)
    list_Fibo= []
    for i in range (1,n+1):
        item_Fibo= Fibo(i)
        list_Fibo.append(item_Fibo)
    return fi, list_Fibo

#print(pick_Fibo(6))
x,y=pick_Fibo(6)
#print(f'f=',x)
#print(f'List to ',y)
