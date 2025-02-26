def calculate_rental_fee(start_hour, end_hour):
    # Đơn giá
    price_first_3_hours = 100000
    discount_price = price_first_3_hours * 0.75  # Giảm 25%
    total_fee = 0
    # Tính số giờ thuê
    rental_hours = end_hour - start_hour
    # Kiểm tra thời gian thuê có nằm trong khoảng giảm giá 10% không
    if 11 <= start_hour < 15 or 11 < end_hour <= 15:
        discount = 0.1  # Giảm 10%
    else:
        discount = 0
    # Tính tiền thuê
    if rental_hours <= 3:
        total_fee = rental_hours * price_first_3_hours
    else:
        total_fee = (3 * price_first_3_hours) + ((rental_hours - 3) * discount_price)
    # Áp dụng giảm giá
    total_fee *= (1 - discount)
    return total_fee
def main():
    while True:
        try:
            start_hour = int(input("Nhập giờ bắt đầu (5 <= giờ bắt đầu <= 22): "))
            end_hour = int(input("Nhập giờ kết thúc (5 <= giờ kết thúc <= 22): "))
            if 5 <= start_hour < end_hour <= 22:
                total_fee = calculate_rental_fee(start_hour, end_hour)
                print(f"Số tiền khách thuê sân tập phải trả là: {total_fee:.0f} đồng")
                break
            else:
                print("Giờ bắt đầu và giờ kết thúc không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
if __name__ == "__main__":
    main()