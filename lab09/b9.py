# Hàm đệ quy để đảo ngược số nguyên
def dao_nguoc_so(n, so_dao=0):
    if n == 0:
        return so_dao
    return dao_nguoc_so(n // 10, so_dao * 10 + n % 10)

# Nhập số nguyên từ bàn phím
n = int(input("Nhập số nguyên n: "))
print("Số đảo ngược là:", dao_nguoc_so(n))
