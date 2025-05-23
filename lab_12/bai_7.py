from datetime import datetime, timedelta

try:
    ngay = input('Nhap ngay - thang - nam(%d-%m-%Y): ')
    date = datetime.strptime(ngay, '%d-%m-%Y')
    ngay_mai = date + timedelta(1)
    print('Ngay mai la:', ngay_mai.strftime('%d-%m-%Y'))

except ValueError as e:
    print('Ngay khong dung')
except:
    print('Loi')