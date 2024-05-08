def gcd(a, b):
    if a == 0 :
        return b
     
    return gcd(b%a, a)
 
a = 26513
b = 32321
print("gcd(", a , "," , b, ") = ", gcd(a, b))  