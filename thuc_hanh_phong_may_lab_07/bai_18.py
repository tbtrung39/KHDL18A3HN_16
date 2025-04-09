#Bài 18:
sinh_vien = {
    input("Nhập số báo danh: "): (
        input("Nhập họ và tên: "),
        float(input("Nhập điểm thi: "))
    )
    for _ in range(int(input("Nhập số lượng sinh viên: ")))
}

so_bao_danh = input("Nhập số báo danh cần tra cứu: ")

if so_bao_danh in sinh_vien:
    print(f"Họ và tên: {sinh_vien[so_bao_danh][0]}, Điểm thi: {sinh_vien[so_bao_danh][1]}")
else:
    print("Số báo danh không tồn tại. Thêm sinh viên vào từ điển.")
    sinh_vien[so_bao_danh] = (
        input("Nhập họ và tên: "),
        float(input("Nhập điểm thi: "))
    )