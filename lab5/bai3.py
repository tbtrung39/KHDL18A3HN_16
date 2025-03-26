so_thap_phan=int(input("Nhap so tu nhien n: "))
so_nhi_phan=''
if so_thap_phan<0:
    print("Vui long nhap lai so tu nhien lon hon 0")
elif so_thap_phan==0:
    print("So thap phan se tra ve 0")
else:
    for i in range(1,so_thap_phan+1,1):
        lay_phan_du=so_thap_phan%2
        so_nhi_phan=so_nhi_phan+str(lay_phan_du)
        #Lay phan nguyen
        so_thap_phan=so_thap_phan//2
        if so_thap_phan==0:
            break
print("So nhi phan: ",so_nhi_phan)