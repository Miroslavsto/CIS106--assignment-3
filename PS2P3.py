def split_amount():
    total_amount = float(input("Enter the total amount received: "))
    amount_per_person = total_amount / 3
    print(f"Each person will receive: ${amount_per_person:.2f}")
split_amount()
