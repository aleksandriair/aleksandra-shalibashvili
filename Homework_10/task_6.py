from datetime import date

def car_info(make, year=date.today().year, **kwargs):
    info = f"Make: {make}, Year: {year}"

    if kwargs:
        for key, value in kwargs.items():
            info += f", {key}: {value}"
    
    return info

print(car_info(make="Subaru", year = 2015, color = "Green", comment = "My first car <3"))
print(car_info(make = "Mercedes-Benz", year = 1955, model = "300 SLR Uhlenhaut Coupe Prototype", price = "$142 million"))
print(car_info(make="Porsche", model = "Cayenne"))