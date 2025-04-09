A = set()
while True:
    ky_tu = input("Nhập ký tự từ bàn phím,'esc' để thoát: ")
    if ky_tu == 'esc':
        break
    A.add(ky_tu)
print("Các kí tự đã nhập: ",A)
A = {x for x in A if not x.isdigit()}
print("Tập hợp sau khi loại bỏ các phần tử số: ",A)