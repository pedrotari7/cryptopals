def hex2base64(hexstr):
    return hexstr.decode('hex').encode('base64')


hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

print hex2base64(hex_str)
