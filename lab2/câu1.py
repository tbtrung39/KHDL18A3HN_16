thang = int(input("Nhap thang: "))
if thang in(1, 3, 5, 7, 8, 10, 12):
    print("Thang co 31 ngay")
elif thang == 2:
    print ("Thang co 28 ngay")
elif thang in(4,6,9,11):
    print("Thang co 30 ngay")
else:
    print("khong hop le.nhap lai.")