# Print number using for loop
for i in range(1,11):
  print(i)

# Print even numbers
for i in range(2,21,2):
  print(i)

# Print odd numbers
for i in range(1,21,2):
  print(i)

# Square star pattern
for i in range(4):
  for j in range(4):
    print("*", end=" ")
  print()

# Right triangle star pattern
for i in range(1,5):
  for j in range(i):
    print("*", end=" ")
  print()

# Inverted right triangle
for i in range(4,0,-1):
  for j in range(i):
    print("*", end=" ")
  print()

# Number pattern
for i in range(1,5):
  for j in range(1,i+1):
    print(j,end=" ")
  print()

# Same number Pattern
for i in range(1,5):
  for j in range(i):
    print(i,end=" ")
  print()
