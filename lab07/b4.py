chieu_cao = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142,
    148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165,
    170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170
]

so_sinh_vien = len(chieu_cao)
tb_chieu_cao = sum(chieu_cao) / so_sinh_vien

chieu_cao_khac_nhau = set(chieu_cao)
tb_chieu_cao_khac_nhau = sum(chieu_cao_khac_nhau) / len(chieu_cao_khac_nhau)

print("Số lượng sinh viên là:", so_sinh_vien)
print("Chiều cao trung bình của sinh viên là:", round(tb_chieu_cao, 2))
print("Chiều cao trung bình (khác nhau) của sinh viên là:", round(tb_chieu_cao_khac_nhau, 2))
