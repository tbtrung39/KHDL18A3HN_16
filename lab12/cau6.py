def kiem_tra_username(username):
    if ' ' in username:
        raise ValueError("Tên người dùng không được chứa dấu cách.")
    if not username.isalnum():
        raise ValueError("Tên người dùng chỉ được chứa chữ cái và chữ số.")
def main():
    danh_sach_email = []
    while True:
        try:
            username = input("Nhập username (nhấn q để dừng): ")
            if username == "q":
                break
            kiem_tra_username(username)
            email = username + "@companyname.com"
            danh_sach_email.append(email)
        except ValueError as loi:
            print("Lỗi:", loi)
        except Exception as e:
            print("Lỗi không xác định:", e)
    print("\nDanh sách email hợp lệ:")
    for email in danh_sach_email:
        print(email)

if __name__ == "__main__":
    main()
