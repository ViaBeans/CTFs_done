k = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
k = bytes.fromhex(k)
k_lst = [i for i in k]
to_check = k_lst[:7]
a = "crypto{"
a = [ord(i) for i in a]
key = [i ^ j for i,j in zip(a, to_check)]
key.append(ord("y"))
flag = []

for i in range(0, 42, 8):
	enc = k_lst[i:i+8]
	dec = [i ^ j for i,j in zip(key, enc)]
	dec_h = [chr(i) for i in dec]
	flag.append(''.join(dec_h))

print(''.join(flag))

