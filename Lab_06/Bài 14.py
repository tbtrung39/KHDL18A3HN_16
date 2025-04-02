mat_khau_dau_vao = "ABd1234@1,a F1#,2w3E*,2We3345"
danh_sach_mat_khau = mat_khau_dau_vao.split(",")
hop_le= []
for mat_khau in danh_sach_mat_khau:
    if 6 <= len(mat_khau) <= 12:
        co_chu_thuong = False
        co_chu_hoa = False
        co_chu_so = False
        co_ky_tu_dac_biet = False
        for ky_tu in mat_khau:
            if 'a' <= ky_tu <= 'z':
                co_chu_thuong = True
            elif 'A' <= ky_tu <= 'Z':
                co_chu_hoa = True
            elif '0' <= ky_tu <= '9':
                co_chu_so = True
            else:
                co_ky_tu_dac_biet = True
        if co_chu_thuong and co_chu_hoa and co_chu_so and co_ky_tu_dac_biet:
            hop_le.append(mat_khau)
print(",".join(hop_le))