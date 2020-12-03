t=int(input())
def check(l,n):
    ans=True
    for k in range(n):
        if l[0][k]!=k+1:
            ans=False
    return ans        
    
    
for _ in range(t):
    c=0
    temp=0
    l=[]
    n=int(input())
    for i in range(n):
        x=list(map(int,input().split()))
        l.append(x)
        
    
    while(not check(l,n)):
            for j in range(n):
                temp=l[j][0]
                l[j][0]=l[0][j]
                l[0][j]=temp
                c=c+1
            print(l)
            break
        
    print(c)     
  
