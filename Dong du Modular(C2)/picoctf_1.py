
def modInverse(a, m):
#nghich dao modul***    
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
 

array = [145, 167 ,233, 272 ,344 ,91, 395 ,393 ,433 ,92, 77 ,414, 344, 318 ,420 ,263 ,87, 186, 96, 103 ,91, 354 ,161  ]
for x  in array:
    print(modInverse(x,41))