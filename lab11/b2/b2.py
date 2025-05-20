def sap_xep_tang_dan():
    # Đọc dữ liệu từ file đầu vào
    with open("inp.txt", 'r') as tep_vao:
        ds_so = list(map(int, tep_vao.read().strip().split()))

    # Sắp xếp tăng dần
    ds_so.sort()

    # Ghi dữ liệu ra file đầu ra
    with open("Out.dat", 'w') as tep_ra:
        tep_ra.write(' '.join(map(str, ds_so)))

# Gọi hàm
sap_xep_tang_dan()
print("Đã sắp xếp xong và ghi ra file Out.dat.")
