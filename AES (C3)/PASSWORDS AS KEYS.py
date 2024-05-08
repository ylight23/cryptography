import binascii,requests,json
from Cryptodome.Cipher import AES
import hashlib
import random
lay_ma= requests.get(f'https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
# # #dinh dang lai ket qua tu json tra ve cho ciphertxt
ma_hoa = lay_ma.json()['ciphertext']
with open("words.txt", 'r') as f:
    #words = [w.strip() for w in f.readlines()]
    for words in f:
        words = words.strip()
        ciphertext = bytes.fromhex(ma_hoa)
        #keyword = random.choice(words)
        key1 = hashlib.md5(words.encode()).hexdigest()
        key = bytes.fromhex(key1)
        print(key)
        cipher = AES.new(key, AES.MODE_ECB)
        decrypt = cipher.decrypt(ciphertext)
        
        if b'crypto{' in decrypt:
            print(decrypt)
            break
#ciphertext = cipher.json()
    
#print(cipher.json())
