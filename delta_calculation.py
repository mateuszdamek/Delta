import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

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