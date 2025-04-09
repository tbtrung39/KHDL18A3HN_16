ds_chieu_cao = [ 161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142,
    148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165,
    170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
so_sv = len(ds_chieu_cao)
print("Số sinh viên trong danh sách: ",so_sv)
chieu_cao_tb = sum(ds_chieu_cao)/so_sv
print(f'Chiều cao trung bình của sinh viên: {chieu_cao_tb:.2f}')
chieu_cao_khac_nhau = set(ds_chieu_cao)
print("Chiều cao khác nhau: ",chieu_cao_khac_nhau)
chieu_cao_khac_nhau_tb = sum(chieu_cao_khac_nhau)/len(chieu_cao_khac_nhau)
print(f'Chiều cao tb khác nhau của các sv: {chieu_cao_khac_nhau_tb:.2f}')
