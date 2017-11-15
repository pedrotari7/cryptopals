
def xor(s1, s2):
    return format(int(s1,base=16) ^ int(s2,base=16), 'x')

s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

for c in xrange(16):
    print xor(s, hex(c)).decode('hex')
