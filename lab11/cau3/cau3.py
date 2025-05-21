def ghi_cuc_tri_vao_file():
    with open("lab11/cau3/f_in.dat", 'r') as tep_vao:
        ds_so = list(map(int, tep_vao.read().strip().split()))
    cuc_tri = []
    for i in range(1, len(ds_so) - 1):
        if (ds_so[i] > ds_so[i - 1] and ds_so[i] > ds_so[i + 1]) or \
           (ds_so[i] < ds_so[i - 1] and ds_so[i] < ds_so[i + 1]):
            cuc_tri.append(ds_so[i])
    with open("f_out.dat", 'w') as tep_ra:
        tep_ra.write(str(len(cuc_tri)) + '\n')
        tep_ra.write(' '.join(map(str, cuc_tri)))
ghi_cuc_tri_vao_file()
print("Đã ghi các cực trị vào file f_out.dat.")