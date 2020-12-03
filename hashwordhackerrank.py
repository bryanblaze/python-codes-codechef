from collections import Counter 
n=int(input())
l=[]
for i in range(n):
    st=input()
    l.append(st)
li=[]
x=Counter(l)
li=set(l)
print(len(set(l)))
for i in x:
    print(x[i],end=" ")

