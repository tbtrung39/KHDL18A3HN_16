ds=[]
while True:
    so=int(input("Nhap so: "))
    if so==0:
        break
    ds.append(so)
print("Danh sach ban dau la:",ds)

chen=[1,2,3]
ds=chen+ds
if len(ds)>=5:
    ds[5:5]=chen
else:
    print("Danh sach chua du 5 phan tu, khong the chen vao vi tri thu 5")
ds+=chen
print("Danh sach sau khi chen la:",ds)

m=int(input("Nhap vi tri can xoa ( tinh tu 0 ): "))
if 0<=m<len(ds):
    del ds[m]
    print(f"Danh sach sau khi xoa phan tu o vi tri {m} la:",ds)
else:
    print("Vi tri khong hop le, khong the xoa")

ds_tang=sorted(ds)
ds_giam=sorted(ds, reverse=True)
print("Danh sach sap xep tang dan:",ds_tang)
print("Danh sach sap xep giam dan:",ds_giam)