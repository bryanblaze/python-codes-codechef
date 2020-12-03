t=int(input())

def makeno(x):
    #nos=['9','8','7','6','5','4','3','2','1']
    i=0
    stri=""
    if int(x)<=9:
        return x
    else:     
            q=x//9
            r=x%9
            for k in range(q):
                stri=stri+'9'
            if(r!=0):
                stri=stri+str(r)
            
        
                
                                                          
           
    return stri
    
    
for _ in range(t):
    
    ch,ri=input().split()

    x=makeno(int(ch))
    y=makeno(int(ri))
    x=str(x)
    y=str(y)
    print(x+" "+y)
    if(len(y)<=len(x)):
        print('1',end=" ")
        print(str(len(y)))
        
    else:
        print('0',end=" ")
        print(str(len(x)))
        
        


        
    
    
  

    
    
