def main():
    try:
        ten_tep_doc = input("Nhập tên tập tin cần đọc: ")
        ten_tep_ghi = input("Nhập tên tập tin mới để ghi nội dung: ")
        try:
            file_doc = open(ten_tep_doc, 'r', encoding='utf-8')
        except Exception as e:
            print(f"Lỗi khi mở tập tin đọc: {e}")
            return
        try:
            file_ghi = open(ten_tep_ghi, 'w', encoding='utf-8')
        except Exception as e:
            print(f"Lỗi khi mở tập tin ghi: {e}")
            file_doc.close()  
            return
        noi_dung = file_doc.read()
        file_ghi.write(noi_dung)
        print("Đã sao chép nd")
    except Exception as e:
        print(f"Có lỗi: {e}")
    finally:
        try:
            file_doc.close()
        except:
            pass
        try:
            file_ghi.close()
        except:
            pass
if __name__ == "__main__":
    main()
