import binascii,requests,json
cipher= requests.get(f'https://aes.cryptohack.org/block_cipher_starter/encrypt_flag')
ciphertext = cipher.json()['ciphertext']
#ciphertext = cipher.json()

print(ciphertext)
a= requests.get(f'https://aes.cryptohack.org/block_cipher_starter/decrypt/{ciphertext}')
b=a.json()['plaintext']

print(b)
print((bytes.fromhex(b)))