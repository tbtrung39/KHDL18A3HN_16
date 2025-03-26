#cách 1 
str = input("Nhập vào chuỗi kí tự: ")
dem_so = 0 
for i in str:
    if "0"<=i<="9":
        dem_so += 1 
print("Các ký tự số trong chuỗi =",dem_so)
#cách 2
chuoi = input("Nhập chuỗi: ")
ky_tu_so = 0
for k in chuoi:
    if k.isdigit():
        ky_tu_so += 1
print("Số chữ số có trong chuỗi là:", ky_tu_so)