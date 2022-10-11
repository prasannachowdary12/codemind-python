t=int(input())
for _ in range(t):
    n=int(input())
    a=n
    while True:
        fc=0
        for i in range(1,a+1):
            if a%i==0:
                fc+=1
        if fc==2:
            break
        a-=1
    b=n
    while True:
        fc=0
        for j in range(1,b+1):
            if b%j==0:
                fc+=1
        if fc==2:
            break
        b+=1
    if n-a<=b-n:
        print(a)
    else:
        print(b)
