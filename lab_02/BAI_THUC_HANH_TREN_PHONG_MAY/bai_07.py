print('Chương trình trình phân loại học lực của học sinh. ') 
print('Nhập điểm học sinh,',end='') 
diem_tk=float(input("điểm:")) 
if 0.0<=diem_tk<=3.0: print("Xếp loại Kém.") 
elif diem_tk==4.0:print("Xếp loại Yếu.") 
elif 5.0<=diem_tk<=6.0:print("Xếp loại Trung bình.") 
elif 7.0<=diem_tk<=8.0:print("Xếp loại Khá.")  
elif 9.0<=diem_tk<=10.0:print("Xếp loại Giỏi.") 
else: 
    print("Nhập sai xin mời nhập lại điểm!")