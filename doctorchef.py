def check(l):
        res=False
        res = all(ele == 0 for ele in l)
        return res

def doctorchef(arr,n,x):
    arr=sorted(arr,reverse=True)
    i=0
    days=0
    
    if(x>=arr[0]):
        days=n
        

    while(not check(arr)):
        print("x "+str(x))
        print("days "+str(days))
        print(arr) 
        j=1
        while j<n:
            if int(arr[j])/int(x)==1:
                x=2*x
                arr[j]=0
                days=days+1
                
                     
            elif((int(arr[j]) < int(x) or int(arr[j]==x)) and (int(arr[j]*2) > int(x) or int(arr[j]*2) ==int(x))):
                x=2*arr[j]
                x=int(x)
                arr[j]=0
                days=days+1
                
           
                
                       
            j=j+1
        cb=arr[0]
        if(arr[0]<=x):
            x=cb*2
            arr[0]=0
           
        else:    
            arr[0]=cb-x
            x=2*x
           
        arr[0]=2*arr[0]
        
        days=days+1
        if(arr[0]>cb):
            arr[0]=cb
        arr=sorted(arr,reverse=True)
    print(days)
    

t=int(input())

for t in range(t):
    
    n,x=input().split()
    n=int(n)
    x=int(x)
    arr=list(map(int,input().split()[:n]))
    doctorchef(arr,n,x)

    
        
    
