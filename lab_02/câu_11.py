def is_valid_date(day, month, year):
    # Kiểm tra tính hợp lệ của ngày
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > days_in_month[month - 1]:
        return False
    return True
def get_next_day(day, month, year):
    # Số ngày trong tháng
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Tính ngày tiếp theo
    if day < days_in_month[month - 1]:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    return day, month, year
def main():
    while True:
        try:
            day = int(input("Nhập ngày (1-31): "))
            month = int(input("Nhập tháng (1-12): "))
            year = int(input("Nhập năm: "))
            if is_valid_date(day, month, year):
                next_day, next_month, next_year = get_next_day(day, month, year)
                print(f"Ngày tiếp theo là: {next_day}/{next_month}/{next_year}")
                break
            else:
                print("Ngày không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
if __name__ == "__main__":
    main()