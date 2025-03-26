str_van_ban = """Chú bé vùng dậy, vươn vai một cái bỗng biến thành một tráng sĩ mình cao hơn trượng, oai phong lẫm liệt. Tráng sĩ bước lên vỗ vào mông ngựa. Ngựa hí dài mấy tiếng vang dội. Tráng sĩ mặc áo giáp, cẩm roi, nhảy lên mình ngựa"""
tu_can_tim = input("Nhập từ đơn cần tìm: ").strip()
tu_trong_van_ban = str_van_ban.split()
so_lan_xuat_hien = tu_trong_van_ban.count(tu_can_tim)
print(f"Từ '{tu_can_tim}' xuất hiện {so_lan_xuat_hien} lần trong đoạn văn.")
