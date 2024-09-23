side_a = int(input("გვერდი 1: "))
side_b = int(input("გვერდი 2: "))
side_c = int(input("გვერდი 3: "))

perimeter = side_a + side_b + side_c
semi_perimeter = 1/2 * perimeter
area = round((semi_perimeter*(semi_perimeter-side_a)*(semi_perimeter-side_b)*(semi_perimeter-side_c))**(1/2),2)

print("ფართობი =", area, ", პერიმეტრი =", perimeter)