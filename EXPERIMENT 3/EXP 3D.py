#w.a.p to accept a digit within 0 to 9 and display the week day such as 0 for sunday , 1 for monday etc
# Program to accept a digit and display the corresponding weekday
# Input a digit from the user
digit = int(input("Enter a digit (0-6) to get the corresponding weekday: "))
# Dictionary mapping digits to weekdays
weekdays = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}
# Display the corresponding weekday or an error message for invalid input
if digit in weekdays:
    print("The corresponding weekday is:", weekdays[digit])
else:
    print("Invalid input! Please enter a digit between 0 and 6.")
    


