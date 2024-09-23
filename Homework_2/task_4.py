speed = input("Please enter the speed: ")

speed = int(speed)

if speed < 0:
    print("The number must be non-negative")
    exit(1)

if speed >= 120:
    print("VERY FAST")
elif speed >= 60:
    print("FAST")
elif speed >= 30:
    print("MODERATE")
elif speed < 30:
    print("SLOW")