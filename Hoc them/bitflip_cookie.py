from base64 import b64decode
from base64 import b64encode
import requests

def bitFlip( pos, bit, data):
    raw = b64decode(data).decode('utf-8')

    list1 = list(raw)
    list1[pos] = chr(ord(list1[pos])^bit)
    raw = ''.join(list1)
    return b64encode(raw)

ck ='a2FoTExMa3dud2txSjByRS9PRFVlaTR5Ylg3dnBSNlp0MkswQytQT253cFJLdnZ4c2RBNExoT2JMK3BSMXUrYTBqelVZZXhOVUlQTFdWdW9aZHNnU3RLLzN3U0J6RlVkVDFzVDVjeVJMTWVUaWtaWXBRdHpTa2tvN3VVRlBLZXU='
for i in range(128):
  for j in range(128):
    c = bitFlip(i, j, ck)
    cookies = {'auth_name': c}
    r = requests.get('http://mercury.picoctf.net:25992/', cookies=cookies)
    if "picoCTF{" in r.text:
      print(r.text)
      break