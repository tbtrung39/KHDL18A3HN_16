char = input("Nhập một ký tự: ")
while char == " " or char == "":
    if char and char[1:] == "":
        print(f"Giá trị ASCII của '{char}' là {ord(char)}")
    else:
        print("Vui lòng nhập một ký tự duy nhất!")