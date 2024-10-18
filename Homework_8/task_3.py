timestamp = input("Please enter a timestamp: ")

date_part, time_part = timestamp.split("T")
year, month, day = date_part.split("-")
time, ms_zone = time_part.split(".")
hour, minute, second = time.split(":")
ms = ms_zone[:6]
zone = ms_zone[-5:]
zone_sign = timestamp[-6]
if int(hour) > 12:
    hour_short = int(hour) - 12
else:
    hour_short = hour

print(f"{day}-{month}-{year} {hour_short}:{minute}:{second} {zone_sign}{zone[1]}")