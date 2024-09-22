import math

def solve_quadratic(a, b, c):
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The roots are real and different: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"The root is real and repeated: {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return f"The roots are complex: {real_part} ± {imaginary_part}i"


print("Quadratic Equation: ax^2 + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


if a == 0:
    print("Coefficient 'a' cannot be zero in a quadratic equation.")
else:

    result = solve_quadratic(a, b, c)
    print(result)
