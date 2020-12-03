from collections  import Counter
if __name__ == '__main__':
    s = input()
    s=list(s)
    c=dict(Counter(s))
    z=0
    a1_sorted_keys = sorted(c, key=c.get, reverse=True)
    for r in a1_sorted_keys:
        if(z<3):
            print(r, c[r])
            z=z+1
        else:
            break
   

    
        
    
