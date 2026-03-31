fruits=["apple","banana","cherry","date","elderberry"]
print("original list:",fruits)
print("element in reverse order with length:")
# for fruit in fruits[::-1]:
#     print(f"fruit:{fruit},length:{len(fruit)}")
reversed_fruit=[fruit[::-1]for fruit in fruits]
print("list with reversed names:")
print(reversed_fruit)