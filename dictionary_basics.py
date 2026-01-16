# Dictionary Basics
# Dictionary stores data in key-value pairs

# Creating a dictionary
student={
  "name":"Muskan",
  "age":20,
  "course":"CSE-AI"
}

print("Student dictionary:",student)

# Accessing values
print("Name:",student["name"])
print("Age:",student["age"])

# Adding a key-value pair
student["year"]="3rd"

# Updating existing value
student["age"]=21

# Removing a key 
student.pop("course")

print("Updated dictionary:",student)

# Getting all keys and values
print("Keys:",student.keys())
print("Values:",student.values())
