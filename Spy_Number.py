n=int(input())
a=str(n)
b=list(a)
s=0
s1=1
for i in b:
    s+=int(i)
    s1*=int(i)
if s==s1:
    print("Spy Number")
else:
    print("Not Spy Number")