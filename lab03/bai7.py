n = int(input("nhập n:"))
S = 0
for i in range(1, n+1):
    S += i**3
print("tổng bậc 3 của {n} số nguyên đầu tiên là ", S)