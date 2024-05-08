import pwn, json,re
r = pwn.remote('0.0.0.0',1111)
#nhận
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())
#gửi
def json_send(hsh):
    request = json.dumps(hsh).encode()
    print(request)
    r.sendline(request)