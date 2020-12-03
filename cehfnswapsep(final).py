t=int(input())

for _ in range(t):
    n=int(input())
    r=0
    summ=(n*(n+1))//2
    hal=summ//2
    if n==0 or n==1 or n==2 or summ%2==1:
        print(0)
    else:
        low=1
        high=n
        while low<high:
            mid=(low+high)//2
            msum=(mid*(mid+1))//2
            if msum==hal:
                r=n-mid
                no=n-r
                r=r+((no)*(no-1))//2+((r)*(r-1))//2
                break
            elif msum<hal:
                low=mid+1
            elif msum>hal:
                r=mid
                high=mid

        if(msum==hal):
            print(r)
        else:
            print(n-r+1)
