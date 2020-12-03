t=int(input())        
for _ in range(t):
    
    n=int(input())
    st=list(map(int,input().split()))
    st1=set(st)

    if len(st)==0:
        print(0)
    else:
        if 0 in st1:
            st1.remove(0)
            print(len(st1))
        else:
            print(len(st1))
        
