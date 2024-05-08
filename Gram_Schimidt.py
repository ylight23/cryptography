
import numpy as np

v=[np.array([4,1,3,-1]),
   np.array([2,1,-3,4]),
   np.array([1,0,-2,7]),
   np.array([6,2,9,-5]),
]
def gram_schmidt():
    ##khoi tao vecto dau tien = vecto thu nhat
    u=[v[0]]
    #truc chuan hoa cac vecto con lai
    for vi in v[1:]:
        mi =[np.dot(vi,uj)/np.dot(uj,uj) for uj in u]
        u+= [vi -sum([mij * uj for (mij,uj) in zip(mi,u)])]
    ##print phan tu thu2 lam tron den thap phan so 5 cua vecto thu 4 sau khi truc chuan hoa
    print(round(u[3][1],5))
print(gram_schmidt())