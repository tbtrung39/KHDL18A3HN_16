start=float(input("giờ bắt đầu thuê sân:"))
finish= float(input("giờ kết thúc thuê sân:"))
hours= finish - start +1
print("số giờ thuê sân là", hours)
if 15<= start and start<= finish and finish<=22:
    if hours>=0.0 and hours<=3.0:
        so_tien_phai_tra= hours*100000 
        print(f"số tiền khác phải trả sau {hours} giờ chơi là:", so_tien_phai_tra)
    else:
        so_tien_phai_tra= 3 * 100000 + (hours - 3) * 75000  
        print(f"số tiền khác phải trả sau {hours} giờ chơi là:", so_tien_phai_tra)
    if 11 <= start  <= 15:
        so_tien_phai_tra *= 0.9 
        print(f"số tiền phải trả là:{so_tien_phai_tra} đồng") 

else:
    print("Giờ nhập vào không hợp lệ. Vui lòng nhập lại.")




