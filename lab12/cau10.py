from datetime import datetime
def main():
    try:
        s1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
        s2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
        d1 = datetime.strptime(s1, "%d-%m-%Y")
        d2 = datetime.strptime(s2, "%d-%m-%Y")
        if d1 > d2:
            d1, d2 = d2, d1
        delta_days = (d2 - d1).days
        years = delta_days // 365
        remaining_days = delta_days % 365
        months = remaining_days // 30
        days = remaining_days % 30
        print(f"Hai ngày cách nhau khoảng: {years} năm, {months} tháng, {days} ngày.")
    except ValueError:
        print("Lỗi,vui lòng dùng dd-mm-yyyy")
if __name__ == "__main__":
    main()
