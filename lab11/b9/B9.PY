def doc_du_lieu(file_in):
    with open(file_in, 'r') as f:
        so_khach = int(f.readline().strip())
        hanh_ly = []
        for _ in range(so_khach):
            dong = f.readline().strip()
            if dong:
                do = list(map(float, dong.split()))
                hanh_ly.append(do)
        return hanh_ly

def tinh_toan_trong_luong(hanh_ly):
    tong_trong_luong = [sum(ds) for ds in hanh_ly]
    return tong_trong_luong

def ghi_file_weight(tong_trong_luong, file_out):
    with open(file_out, 'w') as f:
        for tl in tong_trong_luong:
            f.write(f"{tl:.2f}\n")

def ghi_file_canceled(hanh_ly, tong_trong_luong, file_out):
    with open(file_out, 'w') as f:
        for i, (ds, tong) in enumerate(zip(hanh_ly, tong_trong_luong)):
            if tong > 23 or len(ds) > 5:
                f.write(f"{i+1}\n")

def main():
    hanh_ly = doc_du_lieu("d:\\git\\KHDL18A3HN_16\\thuc_hanh_phong_may_lab11\\Bài 9\\PASSENGER.IN")
    tong_trong_luong = tinh_toan_trong_luong(hanh_ly)
    ghi_file_weight(tong_trong_luong, "WEIGHT.OUT")
    ghi_file_canceled(hanh_ly, tong_trong_luong, "CANCELED.OUT")
    print("Đã xử lý xong hành lý.")

if __name__ == "__main__":
    main()