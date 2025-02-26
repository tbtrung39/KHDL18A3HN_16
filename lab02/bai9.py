so_kw = int(input('Nhập số kw điện tiêu thụ: '))
don_gia = 0
if 0<so_kw<=100:
    don_gia=so_kw*2000
    print("Tiền điện là: ",don_gia)
elif 100<so_kw<=200:
    don_gia=100*2000 + (so_kw-100)*2500
    print("Tiền điện là: ",don_gia)
elif 200<so_kw<=300:
    don_gia=100*2000 + 100*2500 +(so_kw-200)*3000
    print("Tiền điện là: ",don_gia)
elif 300<so_kw:
    don_gia=100*2000 + 100*2500 + 100*3000 + (so_kw-300)*5000
    print("Tiền điện là: ",don_gia)
else: 
    print("Không hợp lệ. Vui lòng nhập lại")