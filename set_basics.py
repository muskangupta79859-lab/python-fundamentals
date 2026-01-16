# SET BASICS
#Set stores unique values and is unordered

# Creating a set
numbers={1,2,3,3,4}
print("Initial set:",numbers)
# duplicates removed automatically

# Adding an element
numbers.add(5)
print("After adding 5:",numbers)

# Removing an element
numbers.remove(2)
print("After removing 2 :",numbers)

# Checking membership
print("Is 3 present in set?", 3 in numbers)

# Length of set
print("Total elements in set:",len(numbers))
