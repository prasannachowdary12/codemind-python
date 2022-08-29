a=int(input())
for i in range(a):
    x=input()
    b=int(x,8)
    c=bin(b)[2:]
    print(c)