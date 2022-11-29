# Use two comma separated inputs from the user
# 1.) user's name
# 2.) a single character

# output - 2 print lines
# 1.) user's name length
# 2.) count the character that user inputed.

# Code -->
name,char = input("Enter your name"),input("Enter a character")
print("Length of user's name is-->",len(name))
print("Character count:",name.count(char))