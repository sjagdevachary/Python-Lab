num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

i = 1
gcd = 1
smallest = min(num1, num2, num3)

while i <= smallest:
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        gcd = i  # update gcd if i divides all three numbers
    i += 1

print(f"The GCD of {num1}, {num2}, and {num3} is {gcd}")
