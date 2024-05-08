from Crypto.PublicKey import RSA
import os
os.chdir("H:")


key = RSA.importKey(open('privacy_enhanced_mail.pem').read())
print(key.export_key)