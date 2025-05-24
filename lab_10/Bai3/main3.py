import sohoc

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
n = int(input("Nhập n để tính tổng ước: "))

print("ƯCLN:", sohoc.Ucln(a, b))
print("BCNN:", sohoc.Bcnn(a, b))
print("Tổng các ước của", n, "là:", sohoc.SumDivisor(n))