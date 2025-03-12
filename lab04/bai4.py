while True:
    tu_so=int(input('Nhap tu so: '))
    mau_so=int(input('Nhap mau so: '))
    if mau_so!=0:
        break
    print('Mau so khong duoc bang 0, vui long nhap lai!')
print(f"Phan so da nhap: {tu_so}/{mau_so}")