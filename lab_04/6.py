so = input("Nhập một số: ")
i = 0
ket_qua = ""
while i < len(so):
    chu_so = so[i]
    if chu_so == '0':
        chu = "không"
    elif chu_so == '1':
        chu = "một"
    elif chu_so == '2':
        chu = "hai"
    elif chu_so == '3':
        chu = "ba"
    elif chu_so == '4':
        chu = "bốn"
    elif chu_so == '5':
        chu = "năm"
    elif chu_so == '6':
        chu = "sáu"
    elif chu_so == '7':
        chu = "bảy"
    elif chu_so == '8':
        chu = "tám"
    elif chu_so == '9':
        chu = "chín"
    else:
        chu = chu_so
    ket_qua = ket_qua + chu
    if i < len(so) - 1:
        ket_qua = ket_qua + " "
    i = i + 1
print("Số", so, "viết bằng chữ là:", ket_qua)