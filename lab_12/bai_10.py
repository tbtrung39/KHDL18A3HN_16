from datetime import datetime
from dateutil.relativedelta import relativedelta

try:
    day1 = input('Nhap ngay thu nhat: ')
    day2 = input('Nhap ngay thu 2: ')
    date1 = datetime.strptime(day1, '%d-%m-%Y')
    date2 = datetime.strptime(day2, '%d-%m-%Y')
    if date1 > date2:
        date1, date2 = date2, date1

    khac = relativedelta(date2, date1)
    print(f'Khoang cach: {khac.years} nam, {khac.months} thang, {khac.days} ngay')

except ValueError:
    print('Thoi gian khong hop le')
except:
    print('Loi')