def gcd(x,y):
    gcd = 1
    if ( x % y ==0 ):
        return y
    else:
        for k in range((y/2),0,-1):
            if (x%k == 0) and (y % k ==0):
                gcd = k
                break
        return gcd


print(gcd(12,18))
