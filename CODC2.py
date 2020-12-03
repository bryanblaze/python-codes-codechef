chef1=0
morty1=0
winners=[]
points=[]
def sod(no):
    sum_of_digits = 0
    for digit in str(no):
            sum_of_digits += int(digit)
    return sum_of_digits        


t=int(input())
for i in range(t):
    chef2=0
    morty2=0
    rounds=int(input())
    for i in range(rounds):
        
        si = list(map(int,input().split()[:2]))
        result=list(map(sod,si))

        chef1=result[0]
        morty1=result[1]
        result=[]
        if(chef1>morty1):
            chef2=chef2+1
        elif(chef1<morty1):
            morty2=morty2+1
        else:
            chef2=chef2+1
            morty2=morty2+1
        
    if(chef2>morty2):
        winners.append(0)
        points.append(chef2)
    elif(chef2<morty2):
        winners.append(1)
        points.append(morty2)
    else:
        winners.append(2)
        points.append(chef2)

for i in range(t):
    print(str(winners[i])+" "+str(points[i]))
    
  
