ngay= int( input(" Nhập ngày: "))
thang= int( input(" Nhập tháng: "))
if thang== 1 or thang== 3 or thang== 5 or thang== 7 or thang== 8 or thang== 10 or thang== 12:
    if 1<= ngay< 31:
        ngay_tiep_theo= ngay+ 1
        print(f" Ngày tiếp theo của {ngay}/ {thang} là {ngay_tiep_theo}/ {thang} ")
    elif ngay== 31:
        ngay_tiep_theo= 1
        thang_tiep_theo= thang+ 1
        print(f" Ngày tiếp theo của {ngay}/ {thang} là {ngay_tiep_theo}/ {thang_tiep_theo}")
    else:
        print(" Không hợp lệ. Nhập lại.")
elif thang== 4 or thang== 6 or thang== 9 or thang== 11:
    if 1<= ngay< 30:
        ngay_tiep_theo= ngay+ 1
        print(f" Ngày tiếp theo của {ngay}/ {thang} là {ngay_tiep_theo}/ {thang} ")
    elif ngay== 30:
        ngay_tiep_theo= 1
        thang_tiep_theo= thang+ 1
        print(f" Ngày tiếp theo của {ngay}/ {thang} là {ngay_tiep_theo}/ {thang_tiep_theo}")
    else:
        print(" Không hợp lệ. Nhập lại.")
elif thang== 2:
    if 1<= ngay< 28:
        ngay_tiep_theo= ngay+ 1
        print(f" Ngày tiếp theo của {ngay}/ {thang} là {ngay_tiep_theo}/ {thang} ")
    elif ngay== 28:
        ngay_tiep_theo= 1
        thang_tiep_theo= thang+ 1
        print(f" Ngày tiếp theo của {ngay}/ {thang} là {ngay_tiep_theo}/ {thang_tiep_theo}")
    else:
        print(" Không hợp lệ. Nhập lại.")
else:
    print(" Không hợp lệ. Nhập lại.")


