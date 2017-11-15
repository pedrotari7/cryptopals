def xor(s1, s2):
    return format(int(s1,base=16) ^ int(s2,base=16), 'x')


s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'

print xor(s1, s2)