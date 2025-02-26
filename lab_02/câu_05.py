def get_month_name(month):
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_names.get(month)
def main():
    while True:
        try:
            month = int(input("Nhập vào tháng (1-12): "))
            if 1 <= month <= 12:
                month_name = get_month_name(month)
                print(f"Tháng {month} là: {month_name}")
                break
            else:
                print("Tháng không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên từ 1 đến 12.")
if __name__ == "__main__":
    main()