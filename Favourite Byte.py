from pwn import xor
#chuyen sang dang hex sang byte
key= bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(0,256):
    flag= xor(key,i)
    #neu ket qua co xuat hien doan ma crypto
    hint = b'crypto'
    if hint in flag:
        print(flag)