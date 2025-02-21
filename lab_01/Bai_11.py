n = int(input("Nhập số lần tung xúc xắc:"))
omega = 6**3
P = 1/omega #Trường hợp cả 3 ra 6
pA = 1 - P  #Trường hợp cả 3 không ra 6
print(f"Xác suất tung {n} lần để cả 3 lần tung xúc sắc có ít nhất 1 lần cả 3 ra 6 là: {(1 - (pA**n)):.2f}")