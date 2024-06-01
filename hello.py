print("hello, world")

# Improving Your First Python Program
input("What is your name?")
print("Hello David Bowie")

# introducing variables
name = input("What's your name? ")
print("hello, name")

"""Multiline comments"""

###Further Improving Your First Python Program###
# Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("hello, " + name)

### We can use a comma , to pass in multiple arguments by editing our code as follows:
# Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("hello,", name)

### Using str
# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)

### more on the print function - does not adds the extra space
# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)