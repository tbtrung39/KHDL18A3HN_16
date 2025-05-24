def hex_to_bin(s):
    return bin(int(s, 16))[2:]

def hex_to_dec(s):
    return int(s, 16)

def bin_to_dec(s):
    return int(s, 2)

def bin_to_hex(s):
    return hex(int(s, 2))[2:].upper()