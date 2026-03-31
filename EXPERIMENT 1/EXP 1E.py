#WRITE A PROGRAM TO INPUT TWO NUMBERS SWAP THEM USING A THIRD VARIABLE AND PRINT THE RESULT
a = int(input("enter first number"))
b = int(input("enter second number"))

temp = a
a = b
b = temp

print("after swapping")
print("first number",a)
print("second number",b)

