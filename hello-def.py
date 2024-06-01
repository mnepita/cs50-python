"""
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")


"""

""" 
name = input("Whats your name?")
hello()
print(name)
"""

# def for define - create own function
"""
def hello(to="world"): #if not parameters is passed, uses as default World
    print("hello,", to)

hello()
name = input("Whats your name?")
hello(name)

"""

# defining a main function
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()