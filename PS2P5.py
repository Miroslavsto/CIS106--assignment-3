def circle_properties():
    radius = float(input("Enter the radius of the circle: "))
    
    pi = 3.174

    area = pi * (radius ** 2)
    
    perimeter = 2 * pi * radius

    print(f"\n--- Circle Properties ---")
    print(f"Radius: {radius}")
    print(f"Area: {area:.2f}")
    print(f"Perimeter (Circumference): {perimeter:.2f}")

circle_properties()

