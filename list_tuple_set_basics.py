#List examples
colors=["red","blue","green"]
print(colors[0])
colors.append("yellow")
print(colors)
colors.remove("blue")
print(colors)


#Tuple examples
numbers=(10,20,30)
print(numbers[1])
#Tuple cannot be changed(immutable)


#Set examples
items={1,2,3,3}
print(items)   #duplicates removed
items.add(4)
print(items)
items.remove(2)
print(items)
