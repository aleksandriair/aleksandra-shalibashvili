def calculate_daily_average(data):
    return tuple(round(sum(day) / len(day), 2) for day in data)

def calculate_daily_max(data):
    return tuple(max(day) for day in data)

def calculate_daily_min(data):
    return tuple(min(day) for day in data)

def calculate_overall_average(daily_averages):
    return round(sum(daily_averages) / len(daily_averages), 2)

def main():
    temperature = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))
    daily_average = calculate_daily_average(temperature)
    daily_max = calculate_daily_max(temperature)
    daily_min = calculate_daily_min(temperature)
    overall_average = calculate_overall_average(daily_average)

    print(f"The daily average temperatures are: {daily_average}")
    print(f"The daily maximal temperatures are: {daily_max}")
    print(f"The daily minimal temperatures are: {daily_min}")
    print(f"The overall average temperature is: {overall_average}")

if __name__ == "__main__":
    main()