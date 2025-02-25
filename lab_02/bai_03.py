thu = int(input("nhập thứ :"))
if 1 <= thu <= 7:
    if thu == 1:
        print("1: sunday")
    elif thu == 2:
        print("2: monday")
    elif thu == 3:
        print("3: tuesday")
    elif thu == 4:
        print("4: wednesday")
    elif thu == 5:
        print("5: thurday")
    elif thu == 6:
        print("6: friday")
    else:
        print("7: saturday")
else:
    print("thư không hợp lệ ! vui lòng nhập lại")
