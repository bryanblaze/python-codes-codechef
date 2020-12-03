   
def minion_game(s):
    st=0
    kev=0
    for i in range(len(s)):
        if(s[i] in 'AEIOU'):
            kev=kev+len(s)-i
        else:
            st=st+len(s)-i    
    if kev>st:
        print("Kevin"+" "+str(kev))
    elif st>kev:    
        print("Stuart"+" "+str(st))
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)
