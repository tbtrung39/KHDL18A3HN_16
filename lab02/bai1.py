a=int(input('Nhập tháng: '))
if a==2:
    print("Tháng",a,"có 28 ngày")
elif a==1 or a==6 or a==9 or a==11:
    print("Tháng",a,"có 30 ngày")
else:
    print("Không hợp lệ. Vui lòng nhập lại")