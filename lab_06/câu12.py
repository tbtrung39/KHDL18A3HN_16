transactions = []  # Danh sách giao dịch
balance = 0
for t in transactions:
    try:
        action, amount = t.split()
        amount = int(amount)
        balance += amount if action == 'D' else -amount
    except ValueError:
        continue

print("Số dư cuối cùng:", balance)