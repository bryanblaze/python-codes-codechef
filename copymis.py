t=int(input())
for i in range(0,t):
    n=int(input())
    
    X=dict();
    Y=dict();
    n=4*n-1
    for i in range(0,n):
        x, y = input().split()
        x = int(x)
        y = int(y)
        if x in X :
            X[x]+=1
        else :
            X[x]=1;
        if y in Y :
            Y[y]+=1
        else :
            Y[y]=1;
         
    for xx in X :
        if (X[xx]%2 != 0) :
            Xco = xx
            break
    for yy in Y :
        if (Y[yy]%2 != 0) :
            Yco = yy
            break
    print(X)
    print(Y)
    for i in X:
        print(i,X[i])
    print(str(Xco)+" "+str(Yco))
           
    
