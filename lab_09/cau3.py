def countdown(seconds):
    if seconds==0:
        print("time's up")
    elif seconds <=120:
        countdown(seconds -1)
print('bat dau dem lui!')
countdown
