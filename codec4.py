def check(l):
        res=False
        res = all(ele == 0 for ele in l)
        return res
def check2(l):
        res=False
        res = all(ele == 0 for ele in l)
        return res
def double(l):
    for i in range(len(l)):
        l[i]=int(l[i])*2

def check1(backup,pop):
        for i in range(len(backup)):
                if(int(backup[i])<int(pop[i])):
                   pop[i]=backup[i]
               
def loopcheck1(popu,x):
        for i in range(1,len(popu)-1):
                if(int(x)>=int(popu[i]) & 2*int(popu[i])>=int(x)):
                        return True
                else:
                        return False
def loopcheck2(popu,x):
        for i in range(1,len(popu)-1):
                if(int(x)<int(popu[i]) ):
                        return True
                else:
                        return False        
        
        


t=int(input())

for i in range(t):
   infected=False
   days=0
   n,x=input().split()
   n=int(n)
   population = list(map(int,input().split()[:n]))
   popu=list(sorted(population,reverse=True))
   print(popu)
   backup=[]
   backup=list(popu)
   if(int(x)>=int(popu[0])):
           days=n
   else:
           while(not infected):
                   if(int(x)>=int(popu[0]) & int(popu[0])!=0):
                           popu[0]=0
                           x=x*2
                           days=days+1
                           print(" dfdfsdf")
                           print(popu)
                           print(" dfdfsdf")
                   else:        
                           
                        if(loopcheck1(popu,x)):
                                           for k in range(1,len(popu)-1):     
                                                   l=[]     
                                                   l.append(popu[k])

                                           l.sort(reverse=True)
                                           p=0     
                                           while(p==len(l)):
                                                   if(int(l[p])<=int(x)):
                                                            x=int(l[p])
                                                            x=x*2
                                                            popu[popu.index(l[p])]=0
                                                            p=len(l)
                                                   else:
                                                           p=p+1
                                           days=days+1
                        elif(loopcheck2(popu,x)):
                                           
                                popu[0]=int(popu[0])-int(x)
                                x=x*2
                                double(popu)
                                check1(backup,popu)
                                days=days+1
                                           
                   print(popu)                        
                   infected=check(popu)
             
   print(days)                
   
    
                       
            
            
            
            

            






            
        
