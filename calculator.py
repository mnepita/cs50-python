# declare some vars 

"""
x = 1
y = 2

z = x + y

print(z)

# make it more interactive 
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
`
"""

"""    
# fixing the bug
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

"""

"""
# improving more the code
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

"""

# define a main function
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()