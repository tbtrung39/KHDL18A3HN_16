#cách1
str = input("Nhập chuỗi kí tự: ")
chuoi_so=""
for c in str:
    if  "0"<=c<="9":
        chuoi_so += c 
so_hoan_hao = 0
if chuoi_so:
    so_nguyen=int(chuoi_so)
    print("Chuỗi số sau khi lọc: ",chuoi_so)
if so_nguyen>0:
    for i in range(1,so_nguyen):
        if so_nguyen %i == 0:
            so_hoan_hao += i
if so_hoan_hao==so_nguyen:
    print("Đây là số hoàn hảo")
else:
    print("Đây không phải số hoàn hảo")
