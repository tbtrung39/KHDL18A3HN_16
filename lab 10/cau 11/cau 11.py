import doicoso1,doicoso2
so = doicoso1.nhap_so()
doicoso1.chuyen_sang_nhi_phan(so)
doicoso1.chuyen_sang_bat_phan(so)
doicoso1.chuyen_sang_thap_luc_phan(so)
 
print("da import thanh cong ")
chuoi= input("nhap chuoi ky tu")
chuoi_loc= doicoso2.loc_ky_tu_hop_le(chuoi)
if not chuoi_loc:
    print("chuoi sau khi loc khog co ky tu hop le")
else:
    print("chuoi sau khi loc ", chuoi_loc)
    he_co_so= doicoso2.xd_co_so(chuoi_loc)
    print("chuoi thuoc he co so ", he_co_so)
    gia_tri = doicoso2.chuyen_sang_he10(chuoi_loc,he_co_so)
    print("gia tri he 10 cua chuoi", gia_tri)