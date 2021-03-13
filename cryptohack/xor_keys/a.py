import codecs
k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k1xk2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2xk3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
fxkall = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

A = hex(((int(fxkall, 16) ^ int(k2xk3, 16)) ^ int(k1, 16)))
print(bytes.fromhex(A[2:]).decode())
print(bytes.fromhex(fxkall).decode())
 
