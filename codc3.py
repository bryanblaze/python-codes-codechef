
#doctorchef
def check(l):
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
               
                   
        
        


t=int(input())



for i in range(t):
    
    infected=False
    days=0
    n,x=input().split()
    n=int(n)
    population = list(map(int,input().split()[:n]))
    backup=list(population)
    l=[]
   
    previous=0               
    
   
        
             
          
    while(not infected):
           days=days+1
           
           if(previous!=0): 
                   previous=int(population[population.index(max(l))])*2
                 
                   for i in range(len(population)):
                           if(days==1):
                            if(int(max(population))>int(x)):
                                    x=int(x)
                                    population[population.index(max(population))]=int(max(population))-int(x)
                                    double(population)
                                    check1(backup,population)
                                    x=x*2
                                    previous=x
                            else:
                                    x=int(max(population))
                                    population[population.index(max(population))]=0
                                    double(population)
                                    check1(backup,population)
                                    x=x*2
                                    previous=x           
                           else:       
                            if(int(population[i])<=int(x) & int(x)>=previous):
                                    l=[]
                                    l.append(population[i])
                                    x=int(max(l))
                                    population[population.index(max(l))]=0
                                    double(population)
                                    check1(backup,population)
                                    x=x*2                         
                            else:
                                    x=int(x)
                                    population[population.index(max(population))]= int(population[population.index(max(population))])-int(x)    
                                    double(population)
                                    check1(backup,population)
                                    x=x*2
                    
                   print(population)
             
                   infected=check(population)        
         
     
         
                 
       
print(days)  
        
        
      
        
        

            

        
        
        
    
        
    
