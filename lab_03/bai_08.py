
for _ in range(1):  
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("n phải lớn hơn 0! Vui lòng chạy lại chương trình.")
    else:
        S1 = n * (n + 1) // 2
        S2 = (n + 1) ** 2
        S3 = n * (n + 1)
        print(f"S1 = {S1}")
        print(f"S2 = {S2}")
        print(f"S3 = {S3}")

