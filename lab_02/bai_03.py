days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_number = 0
while day_number < 1 or day_number > 7:
    day_number = int(input("Nhập số thứ trong tuần (1 - 7): "))
    if day_number < 1 or day_number > 7:
        print("Số thứ không hợp lệ, vui lòng nhập lại!")
print(f"Thứ {day_number} là {days[day_number - 1]}.")
