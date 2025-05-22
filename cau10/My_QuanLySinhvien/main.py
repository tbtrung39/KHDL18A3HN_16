import quanlysinhvien as qlsv
def menu():
    ds=qlsv.doc_file()
    while True:
        print('___MENU__')
        print('1.nhap danh sach sinh vien')
        print('2.tinh diem TL')
        print('3.in danh sach')
        print('4.sap xep theo RL tang dan')
        print('5. in sinh vien co TL cao nhat')
        print('0.thoat')
        chon= input('chon:')
        if chon=='1':
            ds=qlsv.nhap_danh_sach()
            qlsv.ghi_file(ds)
        elif chon=='2':
            print('diem da duoc tinh khi nhap')
        elif chon=='3':
            qlsv.in_danh_sach(ds)
        elif chon =='4':
            ds=qlsv.sap_xep_theo_rl(ds)
            qlsv.in_danh_sach(ds)
        elif chon=='5':
            top=qlsv.sv_tl_cao_nhat(ds)
            qlsv.in_danh_sach(top)
        elif chon=='0':
            break
        else:
            print('lua chon khong hop le')
menu()