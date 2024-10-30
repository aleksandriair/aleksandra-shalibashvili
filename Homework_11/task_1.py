def cels_to_fahr(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

def fahr_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def main():
    print("Temperature converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Please choose an operation (1-2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        result = cels_to_fahr(celsius)
        print(f"{celsius}°C is equal to {result:.1f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahr_to_cels(fahrenheit)
        print(f"{fahrenheit}°F is equal to {result:.1f}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()