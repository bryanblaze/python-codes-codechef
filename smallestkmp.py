
t=int(input())
l=[]
for _ in range(t):
    st=input()
    pat=input()
    st=sorted(sorted(st), key=str.upper)
    
    i=0
    while(i<len(pat)):
        for j in range(len(st)):
            if st[j]==pat[i]:
                st.pop(j)
                break
        i=i+1
    
    for i in range(len(st)):
        if ord(pat[0])<ord(st[i]):
            for j in range(len(pat)):
                st.insert(i,pat[len(pat)-1-j])
            break
    s=""
    l.append(s.join(st))

for _ in range(len(l)):
    print(l[_])
    
    
