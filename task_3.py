a = int(input("გვერდი 1: "))
b = int(input("გვერდი 2: "))
c = int(input("გვერდი 3: "))

peri = a + b + c
s_peri = 1/2 * peri
area = round((s_peri*(s_peri-a)*(s_peri-b)*(s_peri-c))**(1/2),2)

print("ფართობი =", area, ", პერიმეტრი =", peri)