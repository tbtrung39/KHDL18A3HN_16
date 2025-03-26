Str= " Quê hương em nổi tiếng khắp nơi với khu chợ nổi trên sông. Vốn bởi nơi đây có rất nhiều kênh rạch. Người dân di chuyển chủ yếu bằng thuyền, bằng ghe. Vậy nên, mới thành những buổi họp chợ trên mặt nước. Mới đầu, là để phục vụ người dân, sau nó trở thành một nét văn hóa đặc trưng hấp dẫn bà con tứ xứ đến xem. Trên mặt nước dập dềnh, những chiếc thuyền lớn có bé có tè tựu với đủ thứ mặt hàng thơm ngon, hấp dẫn."
tu_don= input("Nhập từ đơn đơn: ")
doan_van= Str.split()
count = 0
for i in doan_van:
    if i == tu_don:
        count= count+ 1
print(f" Số từ {tu_don} trong đoạn văn: {count}")