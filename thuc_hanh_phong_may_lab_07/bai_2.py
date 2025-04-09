#Bài 2:
Numbers = []

while True:
    number = input("Nhập số hoặc khoảng trống để kết thúc: ")
    if number == ' ':
        break
    if number.isdigit():
        Numbers.append(int(number))

print("Numbers: ", Numbers)
print("A: ", set(Numbers))