def loc_ky_tu_hop_le(s):
    hop_le = "0123456789ABCDEF"
    return ''.join([ch.upper() for ch in s if ch.upper() in hop_le])

def la_he_2(s):
    return all(ch in '01' for ch in s)

def la_he_8(s):
    return all(ch in '01234567' for ch in s)

def la_he_10(s):
    return all(ch in '0123456789' for ch in s)

def la_he_16(s):
    return all(ch in '0123456789ABCDEF' for ch in s)

def xac_dinh_he_co_so(s):
    s = s.upper()
    if all(ch in '01' for ch in s):
        return la_he_2
    elif all(ch in '01234567' for ch in s):
        return la_he_8
    elif all(ch in '0123456789' for ch in s):
        return la_he_10
    elif all(ch in '0123456789ABCDEF' for ch in s):
        return la_he_16
    return "Không xác định"

def co_so_2_sang_10(s):
    return int(s, 2)

def co_so_8_sang_10(s):
    return int(s, 8)

def co_so_16_sang_10(s):
    return int(s, 16)
