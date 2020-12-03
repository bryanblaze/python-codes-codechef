import math
t=int(input())
def compute(i):
    return i!=0 and ((i&i-1)==0)
for _ in range(t):
    n=int(input())
    log=math.log(n,2)
    l=[2,3,1]
    if (log).is_integer() and n!=1:
        print('-1')
    elif n==1:
        print('1')
    elif n==3:
        print("2"+" "+"3"+" "+"1")
    elif n==5:
        print("2"+" "+"3"+" "+"1"+" "+"5"+" "+"4")
    
    
    else:
        i=6
        print("2 3 1 5 4 ",end="")
        while(i<=n):
            if compute(i):
                print(str(i+1)+" "+str(i)+" ",end="")
                i=i+2
            else:
                print(str(i)+" ",end="")
                i=i+1

     
    
      
