try:
    t = input()
    t = int(t)
    while (t):
        t -= 1
        n = int(input())
        n = int(n)
        s = input()
        m = dict()
    
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]] = m[s[i]]+1
            else:
                m[s[i]] = 1
        new_string = ""
        for i in range(len(s)):
    
            # if the character has
            # even frequency then skip
            if m[s[i]] % 2 == 0:
                continue
    
            # else concatenate the
            # character to the new string
            new_string = new_string + s[i]
        print(new_string)
        if new_string == "":
            print('YES')
        else:
            print('NO')# cook your dish here
except:
    pass
