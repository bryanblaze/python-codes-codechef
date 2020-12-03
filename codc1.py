#CHEFSTR1
si=[]
n=0
t=0
ans=0
oi=[]
p=0
t=int(input())
for i in range(t):
    si=[]

    n=int(input())
    
     
    
    si = list(map(int,input().split()[:n]))
        
    for j in range(n-1):       
        ans=ans+abs(int(si[j+1])-int(si[j]))-1

 
   
    oi.append(ans)
    ans=0
for i in range(t):    
    print(oi[i])        
   
            
        
        
    
