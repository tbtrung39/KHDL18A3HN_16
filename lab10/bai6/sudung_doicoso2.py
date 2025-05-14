import doicoso2

s=input("nhap chuoi ky tu: ")
s=doicoso2.loc_ki_tu_hop_le(s)
print("chuoi sau khi loai bo ky tu khong hop le: ", s)
print("he co so chuoi la: ", doicoso2.he_co_so(s))

print("nhap chuoi nhi phan: ")
print("=>", doicoso2.nhi_phan_sang_thap_phan(input()))

print("nhap chuoi bat phan: ")
print("=>", doicoso2.bat_phan_sang_thap_phan(input()))

print("nhap chuoi thap luc phan: ")
print("=>", doicoso2.thap_luc_sang_thap_phan(input()))
