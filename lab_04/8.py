ky_tu = input("Nhập một ký tự bất kỳ: ")
while len(ky_tu) != 1:
    print("Vui lòng chỉ nhập một ký tự duy nhất!")
    ky_tu = input("Nhập một ký tự bất kỳ: ")
ma_ascii = ord(ky_tu)
print("Giá trị ASCII của ký tự '", ky_tu, "' là:", ma_ascii)