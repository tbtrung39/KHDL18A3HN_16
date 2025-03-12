while True:
    tu_so = int(input("nhap tu so: "))
    mau_so = int(input("nhap mau so: "))
    if mau_so != 0:
        break
    print("mau so khong duoc bang 0, vui long nhap lai!")

print(f"phan so ban nhap: {tu_so}/{mau_so}")