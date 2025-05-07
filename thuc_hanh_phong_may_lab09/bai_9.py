#Bài 9:
def tinh_so_dao_nguoc(so_n, dao_nguoc=0):
    if so_n == 0:
        return dao_nguoc
    return tinh_so_dao_nguoc(so_n // 10, dao_nguoc * 10 + so_n % 10)

so_n = int(input("Nhập số nguyên n: "))
print(f"Số đảo ngược là: {tinh_so_dao_nguoc(so_n)}")