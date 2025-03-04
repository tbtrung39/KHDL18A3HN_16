#câu1: viết chương trình tính tổng nghịch đảo của số n số nguyên đầu tiên ví dụ....
def tong_nghich_dao(n):
    if n <= 0:
        return "n phải là số nguyên dương!"
    S = sum(1 / i for i in range(1, n + 1))
    return S

n = int(input("Nhập n: "))
print("Tổng nghịch đảo:", tong_nghich_dao(n))