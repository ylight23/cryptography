#dang euclid mo rong: ax + by = gcd(a,b)
def gcd_extended(a,b):
    if a==0:
        return b,0,1 #ket qua gcd = b 
    else:
    #de quy tim x,y
        gcd,x1,y1 = gcd_extended(b%a,a)

    # dang tong quat x,y
        x = y1 - (b//a)*x1 
        y = x1   
        return gcd,x,y

a,b = 26513,32321
GCD, x ,y =gcd_extended(a,b)
print("GCD = ", GCD)
print("x,y = ", x,y)    
print("crypto{",x,",",y,"}")