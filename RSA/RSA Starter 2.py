# encrypt-> ciphertext :c(m)=m^e(mod n)
# decrypt -> plaintext: m(c)=c^d=(m^e)^d (mod n)

m=12 #plain
e=65537 #public key
p=17 #p,q prime
q=23
#=> c=m^e(mod p*q)
print(pow(m,e,p*q))