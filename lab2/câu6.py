def doc_so(n):
    # Danh sách các từ cho các chữ số
    chu_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    # Tách số ra thành hàng trăm, chục, và đơn vị
    hang_tram = n // 100
    hang_chuc = (n % 100) // 10
    hang_don_vi = n % 10
    
    # Chuẩn bị kết quả đọc số
    ket_qua = ""
    
    # Xử lý hàng trăm
    if hang_tram > 0:
        ket_qua += chu_so[hang_tram] + " trăm"
    
    # Xử lý hàng chục
    if hang_chuc > 0:
        ket_qua += " " + chu_so[hang_chuc] + " mươi"
    
    # Xử lý hàng đơn vị
    if hang_don_vi > 0:
        if hang_chuc > 0:  # Nếu có hàng chục, thì không cần "lẻ"
            ket_qua += " " + chu_so[hang_don_vi]
        else:
            ket_qua += " linh " + chu_so[hang_don_vi]
    
    # Trường hợp số có dạng 10, 20, 30, ..., 90
    if hang_chuc == 0 and hang_don_vi == 0 and hang_tram > 0:
        ket_qua = ket_qua.strip()
    
    return ket_qua.strip()

# Nhập vào một số nguyên có ba chữ số
n = int(input("Nhập vào một số nguyên có ba chữ số: "))

# Kiểm tra xem số có thực sự là ba chữ số không
if 100 <= n <= 999:
    print(f"Cách đọc của số {n} là: {doc_so(n)}")
else:
    print("Vui lòng nhập một số nguyên có ba chữ số.")
