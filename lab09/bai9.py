# Hàm đệ quy để đảo ngược số nguyên
def so_dao_ngc(n, so_dao=0):
    if n == 0:
        return so_dao
    return so_dao_ngc(n // 10, so_dao * 10 + n % 10)
n = int(input("Nhập số nguyên n: "))
print("Số đảo ngược là:", so_dao_ngc(n))