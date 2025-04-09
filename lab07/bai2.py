A = set()
while True:
    n = input("Nhập các số tự nhiên,('esc' để thoát): ")
    if n == 'esc':
        break
    A.add(n)
print("Các số tự nhiên của A thuộc numbers: ",A)