#!/usr/bin/env python3

import telnetlib
import json
import sys
HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline())
print(readline())
print(readline())
print(readline())


to_send = {
    "buy": "flag"
}
json_send(to_send)

response = json_recv()

print(response)
print(response["flag"])




    

