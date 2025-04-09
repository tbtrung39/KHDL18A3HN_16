print("Nhập thông tin sinh viên: ")
D = {}
while True:
    ma_sv = input("Nhập mã sv (ấn 'e' để thoát): ")
    if ma_sv == 'e':
        break
    ten = input("Nhập tên sv: ")
    diem = round(float(input("Nhập điểm sinh viên: ")))  
    D[len(D)+1] = {
        "Mã sv": ma_sv,
        "Tên sv": ten,
        "Điểm sv": diem
    }
for i in range(10, -1, -1):
    a = list(filter(lambda x: D[x]["diem sv"] == i, D))
    for k in a:
        print(D[k])
