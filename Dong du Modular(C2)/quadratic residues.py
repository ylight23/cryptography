from math import gcd
# modul luy thua bac cao dang: a^2 = x mod p hay co dang => a^2 -x =k*p 
# dieu kien ucln(p, tap Zp) =1
zn= [i for i in range(1,29) if gcd(29,i) ==1 ]
ints=[14,6,11]
for i in (zn):
    for j in ints:
        for k in range(1,100):
            if(pow(i,2) -j ==k*29):
                print(i)
# ket qua ra 8 va 21                
# de bai yeu cau so nho hon chon 8              