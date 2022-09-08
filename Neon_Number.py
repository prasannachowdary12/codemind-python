n=int(input())
a=n*n
b=str(a)
c=list(b)
s=0
for i in c:
    s+=int(i)
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")