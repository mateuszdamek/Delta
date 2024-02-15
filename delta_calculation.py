import math

while (True):
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        break
    except ValueError as err:
        print("Only numbers are allowed.")
        continue
    
delta = (b**2) - (4*a*c)

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"x1 = {x1}\nx2 = {x2}")
elif delta == 0:
    x1 = -b / (2*a)
    print(f"x1 = {x1}")
else:
    print("Lack of solutions.")