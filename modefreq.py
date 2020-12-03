from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=dict(Counter(l))
    f=sorted(list(c.values()))
    k=Counter(f).most_common(1)
    print(k[0][0])
    
    
