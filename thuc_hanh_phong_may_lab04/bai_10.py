#Bài 10:
so = input("Nhập một số bất kỳ: ")
ket_qua = ""
for chu_so in so:
    if chu_so == '0':
        ket_qua += "không "
    elif chu_so == '1':
        ket_qua += "một "
    elif chu_so == '2':
        ket_qua += "hai "
    elif chu_so == '3':
        ket_qua += "ba "
    elif chu_so == '4':
        ket_qua += "bốn "
    elif chu_so == '5':
        ket_qua += "năm "
    elif chu_so == '6':
        ket_qua += "sáu "
    elif chu_so == '7':
        ket_qua += "bảy "
    elif chu_so == '8':
        ket_qua += "tám "
    elif chu_so == '9':
        ket_qua += "chín "
    elif chu_so == '.':
        ket_qua += "chấm "    
print("Kết quả:", ket_qua)
