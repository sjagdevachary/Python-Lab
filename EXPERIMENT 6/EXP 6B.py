original_dict = {}
num_items = int(input("Enter the number of items for the dict: "))
for i in range(num_items):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value {i+1}: ")
    original_dict[key] = value
swapped_dict = {v: k for k, v in original_dict.items()}
print("Original dictionary:")
print(original_dict)
print("Swapped dictionary:")
print(swapped_dict)
