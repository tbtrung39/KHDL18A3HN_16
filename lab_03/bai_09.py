for _ in range(1):  
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("n phải lớn hơn 0! Vui lòng chạy lại chương trình.")
    else:
        S4 = 0
        S5 = 0
        S6 = 0
        for i in range(1, n + 1):
            S4 += i**2  
        for i in range(1, 2*n + 2, 2):  
            S5 += i**3  
        for i in range(2, 2*n + 1, 2):  
            S6 += i**4  
        print(f"S4 = {S4}")
        print(f"S5 = {S5}")
        print(f"S6 = {S6}")
