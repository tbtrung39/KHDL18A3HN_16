import qly_hanghoa
def main():
    mathangs = []
    n = int(input("Nhap so mat hang: "))
    
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        mathang = qly_hanghoa.nhapthongtinmathang()
        mathangs.append(mathang)
    print("\nDanh sach mat hang truoc khi sap xep theo thue VAT:")
    qly_hanghoa.hienthimathang(mathangs)
    
    mathangssapxep = qly_hanghoa.sapxeptheothue(mathangs)
    
    print("\nDanh sach mat hang sau khi sap xep theo thue VAT giam dan:")
    qly_hanghoa.hienthimathang(mathangssapxep)

if __name__ == "__main__":
    main()

