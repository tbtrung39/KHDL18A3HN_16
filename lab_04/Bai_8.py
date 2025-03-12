ky_tu = input("Nhập một ký tự: ")
while len(ky_tu) != 1:
    ky_tu = input("Vui lòng nhập lại một ký tự duy nhất: ")
gia_tri_ascii = ord(ky_tu)
print(f"Giá trị ASCII của '{ky_tu}' là: {gia_tri_ascii}")