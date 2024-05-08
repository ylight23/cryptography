from pwn import *
import json
import base64
import binascii
import codecs
import sys

#cipher text
# b64_cipher="c3VydmV5c19yb2NrZXRfdGhvc2U="
# rot13_cipher="qnex_qvfgevohgbef_grnzf"
# utf8_cipher = [97, 97, 114, 111, 110, 95, 109, 115, 110, 95, 99, 111, 97, 115, 116]
# bigint_cipher= 0x73686970735f7072696e7465645f63617573696e67
# hex_cipher = "646965745f7461726765745f7375697461626c65"
# #decode & result plaintext
# base64= base64.b64decode(b64_cipher)
# b64_plain = base64.decode("utf-8")
# print("b64: ",b64_plain)

# rot13_plain = codecs.decode(rot13_cipher,"rot-13")
# print("r13: ",rot13_plain)
# utf8_plain = bytes(utf8_cipher).decode("ascii")
# print("utf-8: ",utf8_plain)


# bigint_plain = long_to_bytes(bigint_cipher)
# print("bigint: ", bigint_plain)

# hex_plain = binascii.unhexlify(hex_cipher)
# print("hex: ",hex_plain)
def giai_ma(p, data):
    if p == 'base64':
        return base64.b64decode(data).decode("utf-8")
    elif p =='rot13':
        return codecs.encode(data,"rot-13")
    elif p == 'utf-8':
       return bytes(data).decode("ascii")
    elif p =='hex':
        return binascii.unhexlify(data).decode('utf-8')
    elif p =='bigint':
        return binascii.unhexlify(data.replace('0x', '')).decode('utf-8')


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:

    received = json_recv()
    
    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)

    to_send = {
        "decoded": giai_ma(received["type"], received["encoded"])
    }
    json_send(to_send)
    