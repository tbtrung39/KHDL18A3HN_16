import giaipt

print("Giải phương trình bậc 1: ax + b = 0")
a = float(input("a = "))
b = float(input("b = "))
print("Nghiệm:", giaipt.giai_pt_bac1(a, b))

print("\nGiải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print("Nghiệm:", giaipt.giai_pt_bac2(a, b, c))
