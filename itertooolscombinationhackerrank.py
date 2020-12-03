from itertools import combinations
n=int(input())
arr=list(input().split())
k=int(input())
co=list(combinations(arr,k))
print(co)
total=len(list(co))
noout=0
for i in co:
    if 'a' in i:
        noout=noout+1
print("{:.4f}".format((noout/total)))       
        
        
