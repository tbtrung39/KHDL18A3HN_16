so_thap_phan=int(input("nhap so tu nhien n: "))
so_nhi_phan=''
if so_thap_phan<0:
    print("vui long nhap lai so tu nhien lon hon 0.")
elif so_thap_phan==0:
    print("so thap phan se tra ve 0.")
else:
    for i in range(1,so_thap_phan+1,1):
        lay_phan_du=so_thap_phan%2
        so_nhi_phan=so_nhi_phan+str(lay_phan_du)
        # lay phan nguyen
        so_thap_phan=so_thap_phan//2
        if so_thap_phan==0:
            break
print("so nhi phan: ", so_nhi_phan)