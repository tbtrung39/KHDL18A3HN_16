from datetime import datetime

tuan = ['Thu 2', 'Thu 3', 'Thu 4', 'Thu 5', 'Thu 6', 'Thu 7', 'CHu nhat']
try:
    ngay = input('Nhap ngay - thang - nam(%d-%m-%Y): ')
    date = datetime.strptime(ngay, '%d-%m-%Y')
    day_of_week = date.weekday()
    print('Ngay do la:', tuan[day_of_week])

except ValueError:
    print('Ngay khong hop le.')
except:
    print('Loi')