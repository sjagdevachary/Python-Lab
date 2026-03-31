#w.a.p to input a string "hi ram hi swam hi mam",search the "hi" and replace with hello remove the write space frome the beginning and then display the sentence
# Program to input a string, search and replace, remove whitespace, and display the sentence
# Input the string from the user    
input_string = input("Enter the string 'hi ram hi swam hi mam': ")
# Search for "hi" and replace with "hello"
modified_string = input_string.replace("hi", "hello")
# Remove whitespace from the beginning and end of the string
trimmed_string = modified_string.strip()
# Display the final modified string
print("Modified String:", trimmed_string)