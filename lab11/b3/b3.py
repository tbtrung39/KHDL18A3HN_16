def ghi_cuc_tri_vao_file():
    # Đọc dữ liệu từ file đầu vào
    with open("f_in.dat", 'r') as tep_vao:
        ds_so = list(map(int, tep_vao.read().strip().split()))

    # Tìm các phần tử cực trị
    cuc_tri = []
    for i in range(1, len(ds_so) - 1):
        if (ds_so[i] > ds_so[i - 1] and ds_so[i] > ds_so[i + 1]) or \
           (ds_so[i] < ds_so[i - 1] and ds_so[i] < ds_so[i + 1]):
            cuc_tri.append(ds_so[i])

    # Ghi kết quả ra file đầu ra
    with open("f_out.dat", 'w') as tep_ra:
        tep_ra.write(str(len(cuc_tri)) + '\n')
        tep_ra.write(' '.join(map(str, cuc_tri)))

# Gọi hàm
ghi_cuc_tri_vao_file()
print("Đã ghi các cực trị vào file f_out.dat.")
