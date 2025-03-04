#câu8: viết chương trình nhập n số nguyên dương nếu n<= thì yêu cầu nhập lại  sau đó tính tông các tổng sau
def tinh_tong(n):
    if n <= 0:
        return "n phải là số nguyên dương!"
    S1 = n * (n + 1) // 2
    S2 = n * n
    S3 = n * (n + 1)
    return S1, S2, S3

n = int(input("Nhập n: "))
S1, S2, S3 = tinh_tong(n)
print(f"S1 = {S1}, S2 = {S2}, S3 = {S3}")