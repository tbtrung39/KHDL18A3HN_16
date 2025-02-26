so_nguyen = int(input('Nhập vào một số nguyên có ba chữ số: '))
if so_nguyen < 100 or so_nguyen > 999:
    print('Số không hợp lệ. Vui lòng nhập lại!')
else:
    hang_tram = so_nguyen // 100
    hang_chuc = (so_nguyen % 100) // 10
    hang_don_vi = so_nguyen % 10
    if hang_tram == 1:
        chu_tram = 'một trăm'
    elif hang_tram == 2:
        chu_tram = 'hai trăm'
    elif hang_tram == 3:
        chu_tram = 'ba trăm'
    elif hang_tram == 4:
        chu_tram = 'bốn trăm'
    elif hang_tram == 5:
        chu_tram = 'năm trăm'
    elif hang_tram == 6:
        chu_tram = 'sáu trăm'
    elif hang_tram == 7:
        chu_tram = 'bảy trăm'
    elif hang_tram == 8:
        chu_tram = 'tám trăm'
    elif hang_tram == 9:
        chu_tram = 'chín trăm'

    if hang_chuc == 1:
        chu_chuc = 'mười'
    elif hang_chuc == 2:
        chu_chuc = 'hai mươi'
    elif hang_chuc == 3:
        chu_chuc = 'ba mươi'
    elif hang_chuc == 4:
        chu_chuc = 'bốn mươi'
    elif hang_chuc == 5:
        chu_chuc = 'năm mươi'
    elif hang_chuc == 6:
        chu_chuc = 'sáu mươi'
    elif hang_chuc == 7:
        chu_chuc = 'bảy mươi'
    elif hang_chuc == 8:
        chu_chuc = 'tám mươi'
    elif hang_chuc == 9:
        chu_chuc = 'chín mươi'
    elif hang_chuc == 0:
        chu_chuc = 'lẻ'
