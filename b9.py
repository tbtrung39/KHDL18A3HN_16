num = int(input("nhập vào 1 số nguyên: "))
# chyển số về dương để xử lý tổng chữ số 
num = abs(num)
# tính tổng các chữ số 
sum_digits = 0 
while num > 0:
    sum_digits += num %10 
    num //= 10 
print("tổng các chữ số vừa nhập: ", sum_digits)