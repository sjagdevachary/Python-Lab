# write a program to test a string is palindrome or not
# Program to check if a string is a palindrome
# Input the string from the user
input_string = input("Enter a string to check if it's a palindrome: ")
# Remove spaces and convert to lowercase for accurate comparison
cleaned_string = input_string.replace(" ", "").lower()
# Check if the cleaned string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')