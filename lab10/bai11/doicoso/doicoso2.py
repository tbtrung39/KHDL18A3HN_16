def loc_ki_tu_hop_le(s):
    hop_le="0123456789ABCDEF"
    return ''.join([ch.upper() for ch in s if ch.upper() in hop_le])
def he_co_so(s):
    s=s.upper()
    if all(ch in '01' for ch in s):
        return 2
    elif all(ch in '01234567' for ch in s):
        return 8
    elif all(ch in '0123456789' for ch in s):
        return 10
    elif all(ch in '0123456789ABCDEF' for ch in s):
        return 16
    return "khong xac dinh"

def nhi_phan_sang_thap_phan(s):
    return int(s,2)

def bat_phan_sang_thap_phan(s):
    return int(s,8)

def thap_luc_sang_thap_phan(s):
    return int(s,16)