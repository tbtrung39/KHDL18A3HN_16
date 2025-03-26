#câu2:cho trước(hoặc nhập từ bàn phím) chuỗi ký tự Str, có bao nhiêu ký tự không phải là chữ cái riêng tiếng anh và không là số trong chuỗi Str
S = input("nhap chuoi ky tu: ")
count = 0

for char in S:
    if not char.isdigit():
        count += 1

print("so ky tu khong phai la so trong chuoi:",count)
