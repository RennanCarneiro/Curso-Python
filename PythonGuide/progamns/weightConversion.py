weight = float(input("Enter the weight"))
unit = input("Kilograms, lbs or grams?")

if unit == "Kilograms":
    choice = input("Convert to lbs or grams? ")
    if choice == "grams":
           weight *= 1000
    elif choice == "lbs":
            weight *= 2.20462
    else:
            print("Not valid")
elif unit == "lbs":
    choice = input("Convert to Kilograms or grams? ")
    if choice == "Kilograms":
           weight *= 2.20462
    elif choice == "grams":
            weight *= 0.00220462
    else:
            print("Not valid")
elif unit == "grams":
    choice = input("Convert to lbs or grams? ")
    if choice == "grams":
           weight *= 1000
    elif choice == "lbs":
            weight *= 2.20462
    else:
            print("Not valid")
else:
     print(f"{unit} Not valid")

print(f"Your weight is: {round(weight, 2)} {unit}")
    