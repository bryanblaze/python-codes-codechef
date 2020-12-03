
t=int(input())
l=[]
for _ in range(t):
        s=int(input())
        l.append(s)
        
for k in range(0,len(l)):

        for i in range(0,8):
            print()       
            for j in range(0,8):
                if(i==0 and j==0):
                    print('O',end="")
                    l[k]=int(l[k])-1
                elif(int(l[k])>0):
                    l[k]=int(l[k])-1
                    print('.',end="")     
                else:
                    print('X',end="")
                
            
                
            
                
    
        

    
