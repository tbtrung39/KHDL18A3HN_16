#a
with open('lab11/cau6/sos.txt', 'r') as tep:
    cac_dong = tep.readlines()
    print("Dòng đầu tiên:", cac_dong[0].strip())
    print("Dòng thứ 3:", cac_dong[2].strip())
#b
print("\nToàn bộ nội dung file:")
with open('lab11/cau6/sos.txt', 'r') as tep:
    print(tep.read())
#c
tat_ca_so = []
with open('lab11/cau6/sos.txt', 'r') as tep:
    for dong in tep:
        cac_so = [int(x) for x in dong.strip().split()]
        tat_ca_so.extend(cac_so)
cac_so_le = [str(so) for so in tat_ca_so if so % 2 != 0]
kich_thuoc = 4
so_phan_tu = kich_thuoc * kich_thuoc
ma_tran = []
for i in range(so_phan_tu):
    if i < len(cac_so_le):
        ma_tran.append(cac_so_le[i])
    else:
        ma_tran.append("0")
with open('lab11/cau6/ODD.txt', 'w') as tep:
    for i in range(kich_thuoc):
        dong = ma_tran[i*kich_thuoc : (i+1)*kich_thuoc]
        tep.write(' '.join(dong) + '\n')
with open('lab11/cau6/ODD.txt', 'r') as tep:
    cac_dong = tep.readlines()
    print("\nDòng cuối của ODD.txt:", cac_dong[-1].strip())