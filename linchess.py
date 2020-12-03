t=int(input())
end=[]
for _ in range(t):
    l=[]
    n,k=input().split()
    n=int(n)
    k=int(k)
    steps=float('inf')
    mini=-1
    
    l=list(map(int,input().split()[:n]))
    if k<=0:
        end.append(mini)
    else:    
        for i in range(len(l)):
            if(k%l[i]==0):
                a=k//l[i]
            
                if(float(a)<float(steps)):
                    steps=a
                    mini=l[i]
                
    end.append(mini)        

for _ in range(len(end)):
    print(end[_])
