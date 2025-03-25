Str = input("Nhập chuỗi từ bàn phím: ")
count = 0
for i in Str:
    if '0' <= i <= '9':
        Str = i
        print(Str, end='')
print(' ')
if int(str(Str)) // 2 != 1:
    print("Không phải số hoàn hảo")
else:
    print("Là số hoàn hảo")