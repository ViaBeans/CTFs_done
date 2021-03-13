from pwn import * # pip install pwntools
import codecs
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

got_flag = 0


while got_flag == 0:
	received = json_recv()
	if "flag" in received:
		got_flag = 1
		print(received["flag"])
		exit(0)

	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	a = received["type"]
	b = received["encoded"]
	ret = ""

	if a =="base64":
		ret = (base64.b64decode(b)).decode()
		print(ret)
	elif a == "rot13":
		ret = codecs.decode(b, "rot13")
	elif a == "hex":
		ret = bytes.fromhex(b).decode()
	elif a == "bigint":
		ret = bytes.fromhex(b[2:]).decode()
	else:
		ret = ''.join([chr(i) for i in b])



	to_send = {
	    "decoded": ret
	}
	json_send(to_send)
