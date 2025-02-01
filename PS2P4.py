def car_discount():
    make = input("Enter the car make: ")
    model = input("Enter the car model: ")
    msrp = float(input("Enter the MSRP (price) of the car: "))
    discount_percent = float(input("Enter the discount percent (as a decimal, e.g., 0.15 for 15%): "))
    
    amount_off = msrp * discount_percent
    
    discounted_price = msrp - amount_off
    
    print("\n--- Car Discount Details ---")
    print(f"Make: {make}")
    print(f"Model: {model}")
    print(f"MSRP: ${msrp:.2f}")
    print(f"Discount Percent: {discount_percent * 100:.2f}%")
    print(f"Amount Off: ${amount_off:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")

car_discount()
