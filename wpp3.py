
conversion_factors = [12,  # Inches
                      1/3,  # Yards
                      1/5280,  # Miles
                      304.8,  # Millimeters
                      30.48,  # Centimeters
                      0.3048,  # Meters
                      0.0003048]  # Kilometers

conversion_names = ["Inches", "Yards", "Miles", "Millimeters", "Centimeters", "Meters", "Kilometers"]


length_feet = float(input("Enter the length in feet: "))


print("Conversion options:")
for i, name in enumerate(conversion_names, 1):
    print(f"{i}. {name}")


choice = int(input("Enter the number for your conversion choice: "))


if 1 <= choice <= len(conversion_factors):
    converted_length = length_feet * conversion_factors[choice - 1]
    print(f"{length_feet} feet is equal to {converted_length} {conversion_names[choice - 1]}.")
else:
    print("Invalid choice. Please enter a number between 1 and 7.")
