n= int(input(" Nhập số nguyên dương n: "))
if n<= 0:
    print(" Không hợp lệ. Nhập lại.")
else:
    for i in range( 1, n+ 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print(" " * (n - i) + "*" * (2 * i - 1))
        else:
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
