#Bài 1:
def tim_so_lon_nhat(so1, so2, so3):
    lon_nhat_hai_so = so1 if so1 > so2 else so2
    return lon_nhat_hai_so if lon_nhat_hai_so > so3 else so3

so_thu_nhat = int(input("Nhập số thứ nhất: "))
so_thu_hai = int(input("Nhập số thứ hai: "))
so_thu_ba = int(input("Nhập số thứ ba: "))
ket_qua = tim_so_lon_nhat(so_thu_nhat, so_thu_hai, so_thu_ba)
print(f"Số lớn nhất là: {ket_qua}")