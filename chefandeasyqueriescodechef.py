t=int(input())
for _ in range(t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    l=list(map(int,input().split()))
    qur=0
    i=0
    res=0
   
    while i<n:
        qur=qur+l[i]
        qur=qur-k
        
        if qur<0:
            res=i
            res=res+1
            i=n-1
            break
        i=i+1
    if qur==0:
        res=n+1
    elif qur>0:
        res=n+qur//k
        res=res+1
    print(res)   



'''
import math
t=int(input())
for _ in range(t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    quer=list(map(int,input().split()))
    sumi=sum(quer)
    z=sumi/k
    
        
    if sumi%k==0:
        print(int(sumi/k)+1)
    else:    
        res=math.ceil(z)
        print(int(res))
'''
