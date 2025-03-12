char = input("Nhập một ký tự: ")
if len(char) == 1:
    print("Mã ASCII của ký tự", char, "là:", ord(char))
else:
    print("Vui lòng nhập một ký tự duy nhất.")