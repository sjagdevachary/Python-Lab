# Program to create a dictionary, store sample data, and display its keys and values

# Create a dictionary with sample data
book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genre": "Dystopian"
}

# Display the keys
print("Keys:")
for key in book.keys():
    print(key)

# Display the values
print("Values:")
for value in book.values():
    print(value)

# Display key-value pairs
print("Key-Value pairs:")
for key, value in book.items():
    print(f"{key}: {value}")