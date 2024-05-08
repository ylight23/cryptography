import numpy as np


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b




def Gauss_Reduction(v1,v2):     
     while True:
          if np.linalg.norm(v1)<np.linalg.norm(v2):
               swap(v1,v2)
               m=[(v1.dot(v2))/(v1.dot(v1))]
               if m==0:
                    return(v1,v2)
               
               v2 -=m*v1
v1= np.array([846835985, 9834798552])
v2=np.array([87502093, 123094980])
print(Gauss_Reduction(v1,v2))
print("hello")