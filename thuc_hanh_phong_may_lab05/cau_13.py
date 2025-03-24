#Bài 13:
chuoi_a = input("Nhập chuỗi A: ")
chuoi_b = input("Nhập chuỗi B: ")
co_ket_qua = False
for vi_tri_a in range(1, len(chuoi_a)):
    for vi_tri_b in range(1, len(chuoi_b)):
        phan_truoc_a = int(chuoi_a[:vi_tri_a])
        phan_sau_a = int(chuoi_a[vi_tri_a:])
        phan_truoc_b = int(chuoi_b[:vi_tri_b])
        phan_sau_b = int(chuoi_b[vi_tri_b:])
        if phan_truoc_a + phan_sau_a == phan_truoc_b + phan_sau_b:
            print(f"{phan_truoc_a}+{phan_sau_a}={phan_truoc_b}+{phan_sau_b}")
            co_ket_qua = True
            break
    if co_ket_qua:
        break
if not co_ket_qua:
    print("Không tồn tại cách chia nào thỏa mãn.")