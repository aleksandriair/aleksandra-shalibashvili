def calculate_avg_temp(temperatures: list):
    sum = 0
    for temperature in temperatures:
        sum += temperature
    average_temperature = sum / len(temperatures)
    return average_temperature

def main():
    temperatures = [22, 25, 19, 23, 25, 26, 23]
    average_temperature = calculate_avg_temp(temperatures)
    print(f"The average temperature is {average_temperature}")

if __name__ == "__main__":
    main()