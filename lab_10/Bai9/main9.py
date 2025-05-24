import my_file

ten_file = "vanban.txt"
noi_dung = input("Nhập nội dung ghi vào file: ")

my_file.ghi_file(ten_file, noi_dung)
print("Nội dung trong file:")
print(my_file.doc_file(ten_file))
