n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("n phải lớn hơn 0! Vui lòng chạy lại chương trình.")
else:
    S = 0
    for i in range(1, n + 1):
        S += 1 / i
    print(f"Tổng S = {S:.6f}")
