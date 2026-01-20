# Python Modules - Basics

# Built-in modules

# math module examples
import math
print("Square root of 25:", math.sqrt(25))
print("Power (2^3):", math.pow(2, 3))
print("Value of PI:", math.pi)

print("-" * 30)

# random module examples
import random
print("Random number (1 to 100):", random.randint(1, 100))
numbers = [10, 20, 30, 40, 50]
print("Random choice from list:", random.choice(numbers))

print("-" * 30)

# datetime module examples
import datetime
today = datetime.date.today()
now = datetime.datetime.now()

print("Today's date:", today)
print("Current date & time:", now)

print("-" * 30)

# os module examples
import os
print("Current working directory:", os.getcwd())
