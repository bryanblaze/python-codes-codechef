'''
a = "11011111101100110110011001011101000"
b = "11001011101100111000011100001100001"
y = int(a,2) ^ int(b,2)
print('{0:b}'.format(y))
'''


t=int(input())
final=[]
for _ in range(t):
    n=int(input())
    a=[]
    c=0
    for i in range(n):
        s=input()
        a.append(s)
    if(n==1):
        w3=a[0]
        for z in range(len(w3)):
            if w3[z]=='1':
                c=c+1
        final.append(c)        
    else:   
        for j in range(0,len(a)-1):
            if j==0:
                w1=a[j]
            w2=a[j+1]
       
            w3=int(w1,2)^int(w2,2)
            w3=bin(w3).replace("0b","")
        
            w1=w3
        
        for z in range(len(w3)):
            if w3[z]=='1':
                c=c+1
        
        final.append(c)
        
for _ in range(len(final)):
    print(final[_])
    
