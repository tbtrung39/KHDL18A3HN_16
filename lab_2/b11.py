ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng (1-12): "))

# Xác định số ngày tối đa của tháng
if thang in [1, 3, 5, 7, 8, 10, 12]:  
    max_ngay = 31
elif thang in [4, 6, 9, 11]:  
    max_ngay = 30
elif thang == 2:  
    max_ngay = 28
else:
    print("Tháng không hợp lệ! Vui lòng nhập lại.")
   
# Kiểm tra nếu ngày nhập hợp lệ
if ngay < 1 or ngay > max_ngay:
    print("Ngày không hợp lệ! Vui lòng nhập lại.")
 

# Xác định ngày tiếp theo
if ngay < max_ngay:  # Nếu chưa phải ngày cuối tháng
    ngay += 1
else:  # Nếu là ngày cuối tháng
    ngay = 1
    if thang == 12:  # Nếu là 31/12 -> chuyển sang 1/1
        thang = 1
    else:
        thang += 1

# In kết quả
print("Ngày tiếp theo là:", ngay, "/", thang)