t=int(input())
l=[]
for t in range(t):
    n=int(input())
    text=input()[:n]
    d={}
    c=0
    for k in range(len(text)):
        if text[k] in d:
            d[text[k]]+=1
        else:
            d[text[k]]=1
    addon=""    
    for i in range(len(text)):
        if d[text[i]] % 2==0:
            continue
        
        addon=addon+text[i]
        
    if addon=="":
        l.append('YES')
    else:
        l.append('NO')


for _ in range(len(l)):
    print(l[_])
