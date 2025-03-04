#câu9: viết chương trình nhập n số nguyên dương nếu n<=0 thì yêu cầu nhập lại sau đó tính tống sau bằng vòng lạp for
def tinh_tong_vong_lap(n):
    if n <= 0:
        return "n phải là số nguyên dương!"
    S4 = sum(2 * i for i in range(1, n + 1))
    S5 = sum(2 * i - 1 for i in range(1, n + 1))
    S6 = sum(i ** 2 for i in range(1, n + 1))
    return S4, S5, S6

n = int(input("Nhập n: "))
S4, S5, S6 = tinh_tong_vong_lap(n)
print(f"S4 = {S4}, S5 = {S5}, S6 = {S6}")