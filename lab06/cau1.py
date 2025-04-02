a=[2,-4,1,9,-3,6,3,-2,6,8]
tong=0
count=0
tong1=0
for i in a:
    tong=tong+i
    if i>0:
        count+=1
        tong1+=i
print("tong cua nhung phan tu trong list la: ", tong)
print("so luong nhung so hang duong trong list la: ", count)
print("tong cua nhung so hang duong trong list la: ", tong1)

for i in a:
    if a[i]<0:
        index=a.index(i)
        break
print("vi tri cua phan tu am dau tien: ", index)

gia_tri_max=a[0]
vi_tri_max_cuoi=0
for r in range(len(a)):
    if a[r]>=gia_tri_max:
        gia_tri_max=a[r]
        vi_tri_max_cuoi=r
print("phan tu lon nhat: ", gia_tri_max)
print("vi tri phan tu lon nhat cuoi cung: ", vi_tri_max_cuoi)
