# Python Dictionary - Practice Question Solutions

# 1. Dictionary stores data in key-value pairs
student={"name":"Aman","age":20}
print(student)

# 2.  Create an empty Dictionary
empty_dict={}
print(empty_dict)

# 3. Dictionary to store student's name,age and marks
student={
    "name":"Riya",
    "age":21,
    "marks":85
    }
print(student)

# 4. Access the value of a key
print(student["name"])

# 5. Accessing a non-existing key(will give key error)
#print(student["grade"])

# 6. Add a new key-value pair
student["grade"]="A"
print(student)

# 7. Update value of an existing key
student["marks"]=90
print(student)

# 8. Print all keys of an dictionary
keys=student.keys()
print(keys)

# 9. Print all values of a dictionary
values=student.values()
print(values)

# 10. Iterate over a dictionary
for key,value in student.items():
    print(key,":",value)

# 11. Difference between dict[key] and dict.get[key]
# dict[key] will give key error if does not exist whereas dict.get[key] returns None
print(student.get("age"))
# returns value of key
print(student.get("salary"))
# Returns None

# 12. Check whether a key exists
if  "name" in student:
    print("Key exists")
else:
    print("Key does not exist")

# 13. Delete a key from dictionary
del student["grade"]
print(student)

# 14. Use of items()method
items=student.items()
print(items)

# 15. Count frequency of each character in a string
text="Python"
freq={}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)

# 16. Can dictionary keys be duplicated?
# NO
example={"a":1,"a":2}
print(example)

# 17. Can dictionary values be duplicated?
# Yes
example={"a":1,"b":1}
print(example)

# 18. Merge two dictionaries
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
merged_dict=dict1 | dict2
print(merged_dict)

# 19. Create a dictionary using user input
user_dict={}
key=input("Enter key: ")
value=input("Enter value: ")
user_dict[key]=value
print(user_dict)

# 20. Find the key with maximum value
marks={"Math":80,"Science":90,"English":85}
max_key=max(marks,key=marks.get)
print("Key with maximum value:",max_key)
