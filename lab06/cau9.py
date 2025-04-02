danh_sach=list(map(int,input("nhap danh sach so: ").split()))
for so in danh_sach:
    assert so%2==0, "co so le trong danh sach"
print("tat ca cac so trong danh sach deu la so chan")
