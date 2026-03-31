#write a program to find sum of digi of a posetive integer.
num = int(input("Enter a positive integer: "))
sum = 0

while num > 0:
    digit = num % 10
    sum +=digit
    num //= 10

print("Sum of digits:", sum )
