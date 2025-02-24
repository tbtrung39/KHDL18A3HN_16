print('\n\n\t\t=====chương trình xuất ra ngày tiếp theo của 1 ngày cho trước=====')
ngay = int(input("Nhập ngày cần tìm: "))
thang = int(input("Nhập tháng cần tìm: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang ==12:
    if ngay == 31:
        ngay = 1
        thang += 1
    else:
        ngay += 1
if thang == 4 or thang == 6 or thang == 9 or thang == 11:
    if ngay == 30:
        ngay = 1
        thang += 1
    else:
        ngay += 1 
if thang == 2:
    if ngay == 28:
        ngay = 1
        thang += 1
    else:
        ngay += 1
print("Ngày: ",ngay,"Tháng: ",thang)