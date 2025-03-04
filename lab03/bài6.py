n = int(input("Nhập n từ bàn phím: "))
s = 0 
for i in range(1,n+1):
    s += i**3
print("Tổng bậc 3 của n",n,"Số nguyên đầu tiên là:",s)