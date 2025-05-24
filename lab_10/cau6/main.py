import doicoso2
chuoi = input("Nhap chuoi ky tu: ")
chuoi_loc = doicoso2.loc_chuoi(chuoi)
print("Chuoi sau khi loc:", chuoi_loc)
print("He 2 sang he 10:", doicoso2.he2_sang_he10(chuoi_loc))
print("He 8 sang he 10:", doicoso2.he8_sang_he10(chuoi_loc))
print("He 16 sang he 10:", doicoso2.he16_sang_he10(chuoi_loc))