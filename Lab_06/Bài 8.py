n = int(input("Nhập số phần tử: "))
if n<= 0:
    print(" Không hợp lệ. Nhập lại. ")
else:
    fibonacci = [0, 1]
    for i in range(n - 2):
        so_moi = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(so_moi)
    print(" Dãy Fibonacci: ", ", ".join( map( str, fibonacci[:n])))