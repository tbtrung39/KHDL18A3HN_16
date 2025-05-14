def loc_ky_tu_hop_le(chuoi):
    hop_le= "0123456789ABCDEF"
    chuoi = chuoi.upper()
    return ''.join([c for c in chuoi if c in hop_le])
def xd_co_so(chuoi):
    """ xac dinh co so nho nhat co the ma chuoi hop le nay thuoc ve"""
    max_ky_tu= max(chuoi)
    if max_ky_tu.isdigit():
        co_so= int(max_ky_tu) +1
    else:
        co_so= ord(max_ky_tu)- ord('A') +10 +1
        return max(co_so,2)
def chuyen_sang_he10(chuoi,co_so):
    return(chuoi,co_so)