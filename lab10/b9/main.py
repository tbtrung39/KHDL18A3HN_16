import qly_hang
def main():
    mathangs = []
    n = int(input("Nhap so mat hang: "))
   
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        mathang = qly_hang.nhapthongtinmathang()
        mathangs.append(mathang)
    print("\nDanh sach mat hang truoc khi sap xep theo thue VAT:")
    qly_hang.hienthimathang(mathangs)
   
    mathangssapxep = qly_hang.sapxeptheothue(mathangs)
   
    print("\nDanh sach mat hang sau khi sap xep theo thue VAT giam dan:")
    qly_hang.hienthimathang(mathangssapxep)
 
if __name__ == "_main_":
    main()