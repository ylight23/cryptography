from Crypto.PublicKey import RSA
import os
os.chdir("H:")

key= RSA.import_key(open('bruce_rsa.pub').read())
print(type(key))
print(key.exportKey)
