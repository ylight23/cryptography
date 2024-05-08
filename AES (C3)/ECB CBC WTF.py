import binascii,requests,json
from Cryptodome.Cipher import AES
import hashlib
import random
from Cryptodome.Util.number import long_to_bytes, bytes_to_long

def xor(a, b):
	return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))


def encrypt():
    lay_ma=  requests.get(f'https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag')
# # # #dinh dang lai ket qua tu json tra ve cho ciphertxt
    ciphertext = lay_ma.json()
    return bytes.fromhex(ciphertext['ciphertext'])
    #return ciphertext
def decrypt(cipher):
    url = 'http://aes.cryptohack.org/ecbcbcwtf/decrypt/'
    
    url += cipher.hex() ##url + doan tung doan block cipher de dang hex
    #plaint = requests.get(f'http://aes.cryptohack.org/ecbcbcwtf/decrypt/')
    plaint = requests.get(url)
    plaintext = plaint.json()
    return bytes.fromhex(plaintext['plaintext'])
    #return plaintext

ciphert = encrypt()
iv = ciphert[:16]
cipher1= ciphert[16:32]
cipher2= ciphert[32:]
plain1 = xor(decrypt(cipher1),iv)
plain2 = xor(decrypt(cipher2) , cipher1)
plain = plain1 +plain2
#if b'crypto{' in plain:
print(plain)