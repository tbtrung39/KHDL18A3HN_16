print("\n chương trình tính lương nhân viên dưa theo thâm niên công tác")
TNCT= int(input("nhập tháng thâm niên công tác"))
luong_cơ_ban=1350000
if TNCT<12: 
    luong= luong_cơ_ban*2.34
    print("lương là:",luong)
elif TNCT>=12 and TNCT<36:
    lương=12*2.34+(TNCT-12)*3.33
    print("lương của nhân viên là:",lương)
elif TNCT>=36 and TNCT<60:
    lương=12*2.34+((35-12+1)*3.33)+(TNCT-36)*3.66
    print("lương nhân viên là:",lương)
elif TNCT>=60:
    lương=12*2.34+24*3.33+23*3.66+(TNCT-60)*3.99
    print("lương nhân viên là:",lương)
