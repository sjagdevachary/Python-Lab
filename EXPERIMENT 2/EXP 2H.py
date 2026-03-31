#w.a.p to input "hello world" display in on upper case,lower case, 1st letter capital and find length .
# Program to input "hello world" and display in various formats
# Input the string from the user
input_string = input("Enter the string 'hello world': ")
# Display the string in upper case
upper_case = input_string.upper()
print("Upper Case:", upper_case)
# Display the string in lower case
lower_case = input_string.lower()
print("Lower Case:", lower_case)
# Display the string with the first letter capitalized
capitalized = input_string.capitalize()
print("Capitalized:", capitalized)
# Find and display the length of the string
length = len(input_string)
print("Length of the string:", length)