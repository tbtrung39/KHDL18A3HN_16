a = input("Nhập chuỗi: ")
b = input("Nhập chuỗi: ")
equation = True
while equation:
     if equation:
         for i in a:
             if '0' <= i <= '9':
                 a = i
                 print(a, end='+')
         print('')
         for j in b:
             if '0' <= j <= '9':
                 b = j
                 print(b, end='+')
     else:
         print("Không tồn tại cách đặt")