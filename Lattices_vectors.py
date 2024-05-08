import numpy as np
# tich 2 vecto ki hieu la * => tra ve ket qua la 1 vecto => bai toan tich tich co huong
#a*b = (a1*b1, a2*b2, a3*b3 ,....,an*bn)
# tich vo huong ki hieu la . (dot) => tra ve ket qua la 1 dai so => bai toan tich vo huong
#a.b=(a*b1 + a2*b2 + a3*b3 +... + an*bn)
v= np.array([2,6,3])
w=np.array([1,0,0])
u=np.array([7,7,2])

Y=(3*(2*v-w))
X= 2*u
print(Y)
print(X)
print(np.dot(Y,X)) #vo huong 
print(np.multiply(Y,X)) #co huong

