#!/usr/bin/env python3

import pwn, json,re
from Cryptodome.Hash import SHA256
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
#from utils import listener
from pkcs1 import emsa_pkcs1_v15
#from params import N, E, D

# FLAG = "crypto{?????????????????????????????????}"

# MSG = 'We are hyperreality and Jack and we own CryptoHack.org'
# DIGEST = emsa_pkcs1_v15.encode(MSG.encode(), 256)
# SIGNATURE = pow(bytes_to_long(DIGEST), D, N)


# class Challenge():
#     def __init__(self):
#         self.before_input = "This server validates domain ownership with RSA signatures. Present your message and public key, and if the signature matches ours, you must own the domain.\n"

#     def challenge(self, your_input):
#         if not 'option' in your_input:
#             return {"error": "You must send an option to this server"}

#         elif your_input['option'] == 'get_signature':
#             return {
#                 "N": hex(N),
#                 "e": hex(E),
#                 "signature": hex(SIGNATURE)
#             }

#         elif your_input['option'] == 'verify':
#             msg = your_input['msg']
#             n = int(your_input['N'], 16)
#             e = int(your_input['e'], 16)

#             digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
#             calculated_digest = pow(SIGNATURE, e, n)

#             if bytes_to_long(digest) == calculated_digest:
#                 r = re.match(r'^I am Mallory.*own CryptoHack.org$', msg)
#                 if r:
#                     return {"msg": f"Congratulations, here's a secret: {FLAG}"}
#                 else:
#                     return {"msg": f"Ownership verified."}
#             else:
#                 return {"error": "Invalid signature"}

#         else:
#             return {"error": "Invalid option"}


# listener.start_server(port=13391)


# phần làm 
r = pwn.remote('socket.cryptohack.org',13391)
#nhận
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())
#gửi
def json_send(hsh):
    request = json.dumps(hsh).encode()
    print(request)
    r.sendline(request)

r.recvline()
json_send({"option": "get_signature"})
line =json_recv()
print(line)

msg= 'I am Mallory own CryptoHack.org'
match = re.match(r'^I am Mallory.*own CryptoHack.org$', msg)
print(match)
#băm thông điệp
digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
#xác thực bản băm msg để lấy flag if true
# cho e = 1 , signature =  digest mod n = digest + k*n => cho k =1 => n = signature - digest 
json_send({"option": "verify" ,"msg":msg, "N": hex(int(line["signature"],16) - bytes_to_long(digest)), "e": hex(1) })
flag = json_recv()
print(flag)