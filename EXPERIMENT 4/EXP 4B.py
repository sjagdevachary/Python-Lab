a = 0
b = 1
sum_even = 0
print("Fibonacci series up to 1000:")
while a <= 1000:
    print(a, end=" ")
    if a % 2 == 0:
        sum_even += a
    c = a + b
    a = b
    b = c
print("\nSum of even-valued terms:", sum_even)
