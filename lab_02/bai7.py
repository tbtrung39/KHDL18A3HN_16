diem_tk=float(input("nhap diem thuong ki: "))
if 0.0<=diem_tk<=3.0:
    print("loai kem")
elif 3.0<diem_tk<=5.0:
    print("loai yeu")
elif 5.0<diem_tk<=6.0:
    print("loai trung binh")
elif 6.0<diem_tk<=8.0:
    print("loai kha")
elif 8.0<diem_tk<=10.0:
    print("loai gioi")
else:
    print("khong hop le vui long nhap lai")