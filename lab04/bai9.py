n = int(input("Nhập số nguyên dương n:"))
S = 0 
while n>0:
    S += n%10
    n//=10
print("Tổng các số là:",S)
