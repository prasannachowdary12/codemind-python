def add(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    return sum
a=int(input())
while a>9:
    a=add(a)
print(a)