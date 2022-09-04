import math
t=int(input())
for i in range(t):
    x=int(input())
    a=math.sqrt(x)
    if x%a==0:
        print("True")
    else:
        print("False")