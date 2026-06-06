balance=2500
withdrawal=float(input("Enter the amount to withdraw: "))
if withdrawal<=balance:
    balance-=withdrawal
    print("Withdrawal successful. Remaining balance:",balance)
else:
    print("Insufficient balance. Withdrawal failed.")
