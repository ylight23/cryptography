# cho a,m. tim nghich dao cua a la b
# sao cho a*b ==1 mod m
# vay b la nghich dao modul cua a
# tinh chat modul :
# ->> (a x b) mod m = ((a mod m) x (b mod m)) mod m
import sympy
def mod_inverse(a,m):
    for b in range(1,m):
        if(((a%m) * (b%m)) % m ==1):
            return b
a,m = 85,131
#print(mod_inverse(a,m))
mod_inverse2 = sympy.mod_inverse(1,26)
print(mod_inverse2)
# def pair_inverse(m):
#     for i in range(1,m-1):
#         if(((i%m) * (mod_inverse(i,m)%m)) % m==1):
#             print(i,mod_inverse(i,m))
            
# print(pair_inverse(131))            
