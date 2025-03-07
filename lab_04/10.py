so = input("Nhập một số thập phân: ")
i = 0
ket_qua = ""
while i < len(so):
    ky_tu = so[i]
    if ky_tu == '0':
        chu = "không"
    elif ky_tu == '1':
        chu = "một"
    elif ky_tu == '2':
        chu = "hai"
    elif ky_tu == '3':
        chu = "ba"
    elif ky_tu == '4':
        chu = "bốn"
    elif ky_tu == '5':
        chu = "năm"
    elif ky_tu == '6':
        chu = "sáu"
    elif ky_tu == '7':
        chu = "bảy"
    elif ky_tu == '8':
        chu = "tám"
    elif ky_tu == '9':
        chu = "chín"
    elif ky_tu == '.':
        chu = "phẩy"
    else:
        chu = ky_tu
    ket_qua = ket_qua + chu
    if i < len(so) - 1:
        ket_qua = ket_qua + " "
    i = i + 1
print("Số", so, "viết bằng chữ là:", ket_qua)