sentence=input("enter a sentence:")
list1=sentence.split()
print("list 1 (words) with index using enumerate():")
for index , word in enumerate(list1):
    print("index : {index},world: {word}")
list2=[10,20,30,40,50,60]
print("list2:")
print(list2)
list3=list(zip(list1,list2))
print("list3(combined using zip():")
print(list3)