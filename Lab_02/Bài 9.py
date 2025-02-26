so_KW= int( input(" Nhập số KW: "))
if so_KW < 0:
    print(" Không hợp lệ. Nhập lại.")
elif so_KW >= 0 and so_KW<= 100:
    tien_dien= 2000* so_KW
elif so_KW>= 101 and so_KW<= 100:
    tien_dien= 2000* 100+ ( so_KW- 100) * 2500
elif so_KW>= 201 and so_KW<= 300:
    tien_dien= 2000* 100+ 2500* 100+ ( so_KW- 200) * 3000 
elif so_KW> 300:
    tien_dien= 2000* 100+ 2500* 100+ 3000* 100+ ( so_KW- 300) * 5000
print(" Tiền điện: ", tien_dien) 

