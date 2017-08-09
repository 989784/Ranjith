a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter the number"))
e=int(input("enter the number"))
if((a<b)&(a<c)&(a<d)&(a<e)):
    print("a is small")
elif((b<a)&(b<c)&(b<d)&(b<e)):
    print("b is  small")
elif((c<a)&(c<b)&(c<d)&(c<e)):
    print("c is small")
elif((d<a)&(d<b)&(d<c)&(d<e)):
    print("d is small")
else:
    print("e is  small")
