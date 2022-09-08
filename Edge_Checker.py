a,b=map(int,input().split())
if b==a+1 or a==b+1:
    print("Yes")
elif b==a+9 or b%10==0:
    print("Yes")
elif b==a+9 or a%10==0:
    print("Yes")
else:
    print("No")