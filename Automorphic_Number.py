n=int(input())
a=n*n
b=a%10
c=a%100
d=a%1000
if b==n:
    print("Automorphic Number")
elif c==n:
    print("Automorphic Number")
elif d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")