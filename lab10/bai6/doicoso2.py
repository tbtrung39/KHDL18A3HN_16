def loc_ky_tu_hop_le(s):
    hop_le = "0123456789ABCDEF"
    return ''.join([ch.upper() for ch in s if ch.upper() in hop_le])

def he_co_so(s):
    s = s.upper()
    if all(ch in '01' for ch in s):
        return 2
    elif all(ch in '01234567' for ch in s):
        return 8
    elif all(ch in '0123456789' for ch in s):
        return 10
    elif all(ch in '0123456789ABCDEF' for ch in s):
        return 16
    return "Không xác định"

def co_so2_sang_co_so10(s):
    return int(s, 2)

def co_so8_sang_co_so10(s):
    return int(s, 8)

def co_so16_sang_co_so10(s):
    return int(s, 16)    
    
    
