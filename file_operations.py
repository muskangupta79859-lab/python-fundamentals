# FILE OPERATIONS

# 1. Write Mode (w)-file create / overwrite
file=open("sample.txt","w")
file.write("Hello Python\n")
file.write("This is file handling.")
file.close()

print("File written sucessfully")

# 2. Read Mode (r) -file read
file=open("sample.txt","r")
data=file.read()
file.close()

print("\nReading file:")
print(data)

# 3. Append Mode (a)-data add
file=open("sample.txt","a")
file.write("\nThis line is appended.")
file.close()

print("\nData appended successfully.")

# 4. Read again to check append
file=open("sample.txt","r")
print("\nUpdated file content: ")
print(file.read())
file.close()

# 5. Read line by line
file=open("sample.txt","r")
print("\nReading line by line: ")
for line in file:
  print(line)
file.close()
