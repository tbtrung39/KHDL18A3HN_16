r= float( input(" Nhập bán kính của hình trụ từ bàn phím: "))
h= float( input(" Nhập chiều cao của hình trụ từ bàn phím: "))
dt_xung_quanh= 2* 3.14* r* h
dt_toan_phan= 2* 3.14* r* h+ 2* 3.14* r* r
the_tich= 3.14* r* r* h
print(f" Diện tích xung quanh của hình trụ: {dt_xung_quanh: .2f} ")
print(f" Diện tích toàn phần của hình trụ: {dt_toan_phan: .2f} ")
print(f" Thể tích của hình trụ: {the_tich: .2f} ")