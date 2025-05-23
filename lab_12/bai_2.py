def nhap_ky_tu(ky_tu):
    if not ky_tu.isalpha():
        raise ValueError('Loi ky tu!!!')

    for i in range(len(ky_tu) - 1):
        if ky_tu[i] == ky_tu[i + 1]:
            raise ValueError('Loi nhap lieu!!!')

    for i in range(len(ky_tu) - 3):
        if len(set(ky_tu[i: i + 4])) == 1:
            raise ValueError('Loi nhap lap lai!!!')

        chu = [ky_tu[i: i + 5] for i in range(len(ky_tu) - 4)]
        for i in chu:
            if chu.count(i) > 1:
                raise ValueError('Loi nhap trung lap!!!')

while True:
    try:
        ky_tu = input('Nhap chuoi ky tu: ')
        chuoi = nhap_ky_tu(ky_tu)
        print('CHuoi ky tu:', chuoi)
        break
    except ValueError as e:
        print('Loi:', e)
    except:
        print('Loi')