transactions = []
print("Nhập các giao dịch (D/W số tiền). Nhập 'done' để kết thúc:")
while True:
    entry = input().strip()
    if entry.lower() == 'done':
        break
    transactions.append(entry)

balance = 0
for transaction in transactions:
    parts = transaction.split()
    if len(parts) != 2:
        continue
    action, amount = parts[0], int(parts[1])
    if action == 'D':
        balance += amount
    elif action == 'W':
        balance -= amount

print("Số dư cuối cùng:", balance)