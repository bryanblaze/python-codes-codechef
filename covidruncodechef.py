t=int(input())
for  _  in range(t):
    l=list(map(int,input().split()))
    n=l[0]
    k=l[1]
    x=l[2]
    y=l[3]
    result='NO'
    b=x
    if x==y:
        result="YES"
    else:    
        while((x+k)%n!=b):
            z=(x+k)%n
            x=z

            if z==y:
                result='YES'
    print(result)        
            
