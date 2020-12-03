n,m=map(int,input().split())
l=[]
r=[]
wo=[]
for i in range(n):
    li,ri=map(int,input().split())
    l.append(li)
    l.append(ri)
    wo.append(l)
    l=[]
mi=list(map(int,input().split()))
j=0
count=n

while(count>0):
    for i in range(0,m):   
        if mi[i] in range(wo[j][0],wo[j][1]+1):
            j=j+1
            mi.remove(mi[i])
            i=m-1
            break
        
    
    count=count-1

if j!=n:
    print('NO')
else:
    print('YES')
    
