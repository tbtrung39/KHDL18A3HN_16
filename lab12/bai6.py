def dia_chi_email_nv():
    email_list = []
    while True:
        try:
            username = input("Nhập username: ")
            if ' ' in username or not username.isalnum():
                raise ValueError("Lỗi: Tên nhân viên không được có dấu cách và chỉ bao gồm chữ số và chữ cái.")
            
            email = f"{username}@companyname.com"
            email_list.append(email)
            print(f"Email đã được tạo: {email}")
        
        except ValueError as e:
            print(e)

dia_chi_email_nv()