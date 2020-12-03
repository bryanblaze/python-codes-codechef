t=int(input())
for _ in range(t):
    li=[]
    li=list(map(int,input().split()))
    n=li[0]
    k=li[1]
    l=li[2]
    res=[]
    ans=True
    if(l*k<n):
        print(-1)
    elif l*k>=n and k>1:
        while(ans):
            for i in range(1,k+1):
                if n==0:
                    ans=False
                    break
                
                res.append(i)
                n=n-1
                if n==0:
                    ans=False
                    break
        for z in range(len(res)):
            print(str(res[z])+" ",end="")
        print()
            
    elif n==1 and k==1 and l>=1:
        print(1)
    else:
        print(-1)
         
        
        
        
        
        
    
        
        
        
          
