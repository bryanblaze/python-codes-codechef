t=int(input())
for _ in range(t):
    n1=list(map(int,input().split()))
    n=n1[0]
    x=n1[1]
    p=n1[2]
    k=n1[3]
    l=list(map(int,input().split()))
    l.sort()
    p=p-1
    k=k-1
    if(l[p]==x):
        print(0)
    elif p==k:
        if l[p]<x:
            s=p+1
            while(s<n):
                if l[s]>=x:
                    break
                else:
                    s=s+1
            print(s-p)        
        else:
            s=p-1
            while s>=0:
                if l[s]<=x:
                    break
                else:
                    s=s-1
            print(p-s)
    elif p<k:
        if l[p]<x:
            print(-1)
        else:
            s=p-1
            while s>=0:
                if l[s]<=x:
                    break
                else:
                    s=s-1
            print(p-s)
    else:
        if l[p]<x:
            s=p+1
            while(s<n):
                if l[s]>=x:
                    break
                else:
                    s=s+1
            print(s-p)
        else:
            print(-1)

                


            
                    
