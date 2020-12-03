
t=int(input())
ar=[]
for _ in range(t):
    li=[]
    l=[]
    n,s=input().split()
    n=int(n)
    string=""
    l = list(map(int,input().split()[:n]))
    for i in range(len(l)):
        if int(l[i])%int(s)==0:
            li.append('1')
        else:
            li.append('0')
    s=''
    s=s.join(li)
    ar.append(s)
    
for k in range(len(ar)):
    print(ar[k])
            
           
