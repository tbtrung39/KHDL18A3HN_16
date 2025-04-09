set1= set()
while True:
    n= input(" Nhập kí tự từ bàn phím: ")
    if n.upper()== "ESC":
        break
    set1.add(n)
print(" Tập hợp kí tự: ", set1)
for char in set1.copy():
    if char.isdigit():
        set1.remove(char)
print(" Tập hợp sau khi xóa những phần tử là số: ", set1)