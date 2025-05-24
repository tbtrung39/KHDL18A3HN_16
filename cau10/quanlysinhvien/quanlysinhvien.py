import csv
FILE_PATH='ds_sinhvien.csv'
def tinh_tinh_luy(tb,rl):
    return(tb,rl)/2
def doc_file():
    ds=[]
    try:
        with open(FILE_PATH, newline='',encoding='utf-8')as f:
            reader=csv.DictReader(f)
            for row in reader:
                row['TB']=float(row['TB'])
                row['RL']=float(row['RL'])
                row['TL']=float(row['TL'])
                ds.append(row)
    except FileNotFoundError:
        pass
    return ds
def ghi_file(ds):
    with open(FILE_PATH,'w',newline='',encoding='utf-8')as f:
        fieldnames=['ma sv','ho ten','tb','rl','tl']
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        for sv in ds:
            writer.writerow(sv)
def nhap_danh_sach():
    ds=[]
    n=int(input('nhap so luong sinh vien:'))
    for _ in range(n):
        ma=input('ma sv:')
        ten=input('ho ten:')
        tb= float(input('diem tb:'))
        rl=float(input('diem rl:'))
        tl=tinh_tinh_luy(tb,rl)
        ds.append({'ma sv': ma, 'ho ten':ten,'TB': tb,'RL': rl,'TL':tl})
    return ds
def in_danh_sach(ds):
    print(f'{'ma sv':<10}{'ho ten':<20}{'TB':<10}{'RL':<10}{'TL':<10}')
    for sv in ds:
        print(f"{sv['ma sv']:<10}{sv['ho ten']:<20'}{sv['TB']:<10.2f}{sv['RL']:<10.2f}{sv['TL']:<10.2f}")
def sap_xep_theo_rl(ds):
    return sorted(ds, key=lambda sv: sv['RL'])
def sv_tl_cao_nhat(ds):
    max_tl=max(ds,key=lambda sv: sv['TL'])['TL']
    return [sv for sv in ds if sv['TL']== max_tl]