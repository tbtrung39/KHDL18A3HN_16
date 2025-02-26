print('\n Chương trình tính lương nhân viên dựa theo thâm niên công tác')
TNCT=int(input('Nhập tháng thâm niên công tác: '))
luong_co_ban=1350000
if TNCT<12:
    luong=luong_co_ban*2.34
    print("Lương của nhân viên là:",luong)
elif 12<=TNCT<36:
    luong=12*2.34+(TNCT-12)*3.33
    print("Lương của nhân viên là:",luong)
elif 36<=TNCT<60:
    luong=12*2.34+((35-12+1)*3.33)+(TNCT-36)*3.66
    print("Lương của nhân viên là:",luong)
elif TNCT>=60:
    luong=12*2.34+24*3.33+23*3.66+(TNCT-60)*3.99
    print("Lương của nhân viên là:",luong)