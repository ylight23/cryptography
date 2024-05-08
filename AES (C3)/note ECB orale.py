import requests,binascii,json
import string,time
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad



def get_ciphertext(payload):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    url += payload.hex()
    url += '/'
    r = requests.get(url)
    ct = (json.loads(r.text))['ciphertext']
    return ct
#15 first bytes of flag

# flag = "crypto{p3n6u1n5"
# alphabet = '_'+'@'+'}'+string.digits+string.ascii_lowercase+string.ascii_uppercase
# while(1):
#     plaintext = "1"*(31-len(flag))
#     up = plaintext.encode("utf-8")
#     print(up, len(up),flag)
#     ct = get_ciphertext(up)
#     for char in alphabet:
#         check= get_ciphertext((plaintext +flag + (char)).encode("utf-8"))
#         print((char))
#         if(check[32:64] == ct[32:64]):
#             flag += (char)
#             print(flag)

#             break
# n=31

flag= ''
# while(1):
#     plaintext ='0'*(15-len(flag)) #(plain--) + (char++) = block(flag) 16 byte
#     ct= get_ciphertext((plaintext).encode('utf-8'))
#     alphabet = '_'+'@'+'}'+'{'+string.digits+string.ascii_lowercase+string.ascii_uppercase
#     for char in alphabet:
#         if(get_ciphertext((plaintext +flag+ char).encode('utf-8'))[:32]== ct[:32]): #check 32 hexa dau tien
#            flag += char
#            print(flag)
#            break
#         time.sleep(1)
#     #print(flag)
         
#flag2 = 'crypto{p3n6u1n5'

flag= ''

while(1):
    plaintext = "0"*(31-len(flag))
    ct = get_ciphertext((plaintext).encode("utf-8"))
    alphabet = '_'+'@'+'}'+'{'+string.digits+string.ascii_lowercase+string.ascii_uppercase
    for char in alphabet:
    #for char in range(33, 127):
        if(get_ciphertext((plaintext + flag + char).encode("utf-8"))[32:64] == ct[32:64]): #check 32->64 hexa (block thu 2)
            flag += (char)
            print(flag)
            if (char) == '}':
                exit()
            break

