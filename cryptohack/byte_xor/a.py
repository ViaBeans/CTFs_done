import codecs
string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
string = bytes.fromhex(string)

str = [i for i in string]
for i in range(0, 256):
    flag = [chr(j ^ i) for j in str]
    fleg = ''.join(flag)
    if fleg[0:6] == "crypto":
        print(fleg)
