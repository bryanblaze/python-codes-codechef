import math
t=int(input())
l=[]
for _ in range(t):
    h,p=input().split()
    h=int(h)
    p=int(p)

    while(h>0 and p>0):
        h=h-p
 
        if(h>0):
            p=p/2
            p=math.floor(p)

    if(h<=0):
        l.append(1)
    else:
        l.append(0)


for _ in range(len(l)):
    print(l[_])
