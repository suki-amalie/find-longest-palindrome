from unicodedata import name


def manacher(s):
    temp = '#'.join('^{}$'.format(s))
    print("reformatted s", temp)
    n = len(temp)
    print("n", n)
    p =[0]*n # i's radius which also include i, Ex: s= $aba^ -> p[2] = 2
    print("output for p", p)
    l = r = 1
    for i in range(1, n-1):
        # if the radius of the mirror pos of i exceeds the boundary of the "outer palindrom"
        # then p[i] is restricted to fit inside the "outer palindrom"
        # if the radius of the mirror pos of i stays within the outer palindrom
        # then set p[i] to be the size of its mirror position
        # if i is outside of the outer palindrom
        # then initialized p[i] to be 0 and use trivial algorithm to calculate its radius
        p[i] = max(0, min(r-i, p[l + (r-i)]))  
        while temp[i - p[i]] == temp[i + p[i]]:
            print(i, p[i], p)
            p[i] += 1
        
        # update the boundaries of outer palindrome
        if i + p[i] > r:
            l = i - p[i]
            r = i + p[i]
            print("update boundaries", l, r)
    center_I = max([(i, r) for i, r in enumerate(p)], key=lambda x: x[1])[0]
    max_r = max(p)-1
    print("center index", center_I)
    return s[(center_I-max_r)//2:(center_I + max_r)//2]


s = "abababc"
print(manacher(s))