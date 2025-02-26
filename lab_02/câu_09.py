def calculate_electricity_bill(kwh):
    if 0 <= kwh <= 100:
        price_per_kwh = 2000
    elif 101 <= kwh <= 200:
        price_per_kwh = 2500
    elif 201 <= kwh <= 300:
        price_per_kwh = 3000
    elif kwh > 300:
        price_per_kwh = 5000
    else:
        return None  # Trường hợp không hợp lệ
    total_bill = kwh * price_per_kwh
    return total_bill
def main():
    while True:
        try:
            kwh = float(input("Nhập số KW điện tiêu thụ: "))
            if kwh < 0:
                print("Số KW không hợp lệ. Vui lòng nhập lại.")
                continue
            bill = calculate_electricity_bill(kwh)
            print(f"Tổng tiền điện phải trả là: {bill} đồng")
            break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
if __name__ == "__main__":
    main()