
t=int(input())


for t in range(0,t):
    x=dict()
    y=dict()

    n=int(input())
    r=4*n-1

    for i in range(r):
        xi,yi=input().split()
        
        if xi in x:
            x[xi]=int(x[xi])+1
        else:
            x[xi]=1
            
        if yi in y:
            y[yi]=int(y[yi])+1
        else:
            y[yi]=1
    for j in x:
        if(int(x[j])%2!=0):
            fx=j
            break
    for k in y:
        if(int(y[k])%2!=0):
            fy=k
            break

    print(fx,fy)    
