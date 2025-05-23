def tinh_S1(n):
    if n == 1:
        return 1
    return n + tinh_S1(n - 1)
def tinh_S2(n):
    if n == 1:
        return 1
    return n * n + tinh_S2(n - 1)
def main():
    try:
        n = input("Nhập số nguyên dương n: ")
        if not n.isdigit():
            raise ValueError("n phải là số nguyên dương")
        n = int(n)
        if n <= 0:
            raise ValueError("n phải là số nguyên dương lớn hơn 0")
        tong1 = tinh_S1(n)
        tong2 = tinh_S2(n)
        print(f"Tổng S1 = {tong1}")
        print(f"Tổng S2 = {tong2}")
    except ValueError as ve:
        print("Lỗi giá trị:", ve)
    except RecursionError:
        print("Lỗi: Đã xảy ra lỗi đệ quy (n quá lớn).")
    except Exception as e:
        print("Lỗi không xác định:", e)
if __name__ == "__main__":
    main()
