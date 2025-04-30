def so_dao_nguoc(n, rev=0):
    if n == 0:
        return rev
    return so_dao_nguoc(n//10, rev*10 + n%10)

n = int(input("Nhập số nguyên n: "))
print("Số đảo ngược là:", so_dao_nguoc(n))