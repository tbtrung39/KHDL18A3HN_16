def so_dao_nguoc(n, rev=0):
    if n == 0:
        return rev
    return so_dao_nguoc(n//10, rev*10 + n%10)

n = int(input("Nhap so nguyen n: "))
print("So dao nguoc la:", so_dao_nguoc(n))