def gcd_extended(a,b):
    if(b==0):
        return a
    else:
        return gcd_extended(b,a%b)
a,b= 273246787654, 65537
print(gcd_extended(a,b))
    
