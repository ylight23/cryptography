from Cryptodome.PublicKey import RSA
import os

os.chdir('H:')

key = RSA.importKey(open('2048b-rsa-example-cert.der', 'rb').read())
print(key.export_key)
