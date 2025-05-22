with open('dayso.dat','w')as f:
    f.write('4 5 6\n7 8 9\n10 11')
def tinh_tong_day_so(filename):
    try:
        with open(filename,'r')as file:
            data= file.read().split()
            numbers=[int(num)for num in data]
            tong_tat_ca=sum(numbers)
            tong_le=sum(num for num in numbers if num %2!=0)
            print('tong cac so trong file la:',tong_tat_ca)
            print('tong cac so le trong file la:',tong_le)
    except FileNotFoundError:
        print('khong tim thay file')
    except ValueError:
        print('file co chua du lieu khong hop le')
tinh_tong_day_so('dayso.dat')