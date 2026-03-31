#w.a.p to input data for int , string ,float boolean comlex and then display their datatype.
# Program to input data of various types and display their datatypes
# Input an integer
int_data = int(input("Enter an integer: "))
print("Data:", int_data, "| Type:", type(int_data))
# Input a string
str_data = input("Enter a string: ")
print("Data:", str_data, "| Type:", type(str_data))
# Input a float
float_data = float(input("Enter a float: "))
print("Data:", float_data, "| Type:", type(float_data))
# Input a boolean
bool_data = input("Enter a boolean (True/False): ")
bool_data = True if bool_data.lower() == 'true' else False
print("Data:", bool_data, "| Type:", type(bool_data))
# Input a complex number
complex_data = complex(input("Enter a complex number (e.g., 1+2j): "))
print("Data:", complex_data, "| Type:", type(complex_data))
