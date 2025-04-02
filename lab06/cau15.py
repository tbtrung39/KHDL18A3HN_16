n=int(input("nhap so luong nguoi: "))
data=[]
for i in range(n):
    user=input(f"nhap vao thong tin nguoi thu {i+1} (name, age, height): ")
    name,age,height=user.split(",")
    name=name.strip()
    age=int(age.strip())
    height=float(height.strip())
    data.append((name,age,height))

data.sort(key=lambda x:(x[0],x[1],x[2]))
print("danh sach sau khi sap xep: ")
for item in data:
    print(item)