month = int(input("Nhập vào một tháng (1-12): "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(f"Tháng {month} có 31 ngày.")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f"Tháng {month} có 30 ngày.")
elif month == 2:
    print(f"Tháng {month} có 28 ngày.")
else:
    print("Tháng không hợp lệ. Vui lòng nhập từ 1 đến 12.")
