n = input("Nhập 1 số tự nhiên từ bàn phím: ")
decimal = True
for i in n:
    if i == '0' and i == '1':
        decimal = False
        break

if decimal:
    binary = 0
    for i in range(len(n)):
        binary = int(str(i)) // 2
    print("Số nhị phân tương ứng là:", binary, end='')
else:
    print("Không phải là chuỗi thập phân")