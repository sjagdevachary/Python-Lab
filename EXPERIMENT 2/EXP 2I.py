#w.a.p to input a string "good morning friends how are you all" and do the opertion display in reverse order of character , split whole sentence into individual words and store.
# Program to input a string and perform various operations
# Input the string from the user
input_string = input("Enter the string 'good morning friends how are you all': ")
# Reverse the string using slicing
reversed_string = input_string[::-1]
# Display the reversed string
print("Reversed String:", reversed_string)
# Split the string into individual words
words_list = input_string.split()
# Display the list of words
print("List of Words:", words_list)