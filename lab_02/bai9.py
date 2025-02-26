n=int(input("nhập số (Kw) điện tiêu thụ:"))
tien_dien=0
if n<=100:
    tien_dien=n*2000
    print("tien dien thang nay là:", tien_dien)
elif n>=101 and n<=200:
    tien_dien=100*2000+(n-100)*2500
    print("tiền điện tháng này là:", tien_dien)
elif n>=201 and n<=300:
    tien_dien=100*2000+100*2500+(n-200)*3000
    print("tiền điện tháng này là:", tien_dien)
elif n>300:
    tien_dien=100*2000+100*2500+n*3000+(n-300)*5000
    print("tiền điện tháng này là:", tien_dien)
else:
    print("không hợp lệ. Xin vui lòng nhập lại")
    


