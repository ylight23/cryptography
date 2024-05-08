import numpy as np


def Gauss_Reduction(v1,v2):     
     while True:
          if np.linalg.norm(v2)<np.linalg.norm(v1):
               v1,v2=v2,v1
          m=int((v1.dot(v2))/(v1.dot(v1)))
          if m==0:
               return(v1,v2)
          else:     
               v2 =v2- m*v1
v1= np.array([846835985, 9834798552],dtype='int64')
v2=np.array([87502093, 123094980],dtype='int64')
print(Gauss_Reduction(v1,v2))
#lay ket qua sau khi gauss reduction
a1=np.array([ 87502093, 123094980], dtype='int64')
a2=np.array([-4053281223,  2941479672],dtype='int64')
#nhan vecto 2 ketqua tren se ra FLAG
print(a1.dot(a2))
