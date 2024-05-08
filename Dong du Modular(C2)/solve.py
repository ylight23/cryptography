cipher = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"


def tohex(c,key):
    res = []
    for i in range(0,len(c)//2,2):
        res.append(int(cipher[i:i+1],16))
    print(res)

# for c in range(0,100):
print(tohex(cipher,0x10))
    
