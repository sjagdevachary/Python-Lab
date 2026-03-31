#w.a.p to input 3 co-efficients values and find the real root.
# Program to input 3 coefficients and find the real roots of a quadratic equation
import cmath
# Input coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))   
c = float(input("Enter coefficient c: "))
# Calculate the discriminant
discriminant = b**2 - 4*a*c
# Calculate the two roots using the quadratic formula
root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
# Display the roots
print("The roots of the quadratic equation are:")
print("Root 1:", root1)
print("Root 2:", root2)