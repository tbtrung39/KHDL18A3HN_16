n = int(input("nhập n: "))
S = 1
for i in range(1, n+1):
    S += (2*(i+1)) / (2*i+3)
print("tổng S =", round(S, 3))