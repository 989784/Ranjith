a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter the number"))
e=int(input("enter the number"))
if((a>b)&(a>c)&(a>d)&(a>e)):
    print("a is large")
elif((b>a)&(b>c)&(b>d)&(b>e)):
    print("b is large")
elif((c>a)&(c>b)&(c>d)&(c>e)):
    print("c is large")
elif((d>a)&(d>b)&(d>c)&(d>e)):
    print("d is large")
else:
    print("e is large")
