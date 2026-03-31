# w.a.p to find the gretest among 3 unequa numbers.
# Program to find the greatest among 3 unequal numbers
# Input three unequal numbers from the user
num1 = float(input("Enter first unequal number: "))
num2 = float(input("Enter second unequal number: "))
num3 = float(input("Enter third unequal number: "))
# Determine the greatest number using conditional statements
if num1 > num2 and num1 > num3:
    greatest = num1
elif num2 > num1 and num2 > num3:
    greatest = num2
else:
    greatest = num3
# Display the greatest number
print("The greatest number among the three is:", greatest)