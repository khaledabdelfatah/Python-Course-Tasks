#Write a program to create function calculation() 
#such that it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.

def perform_calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

 
x=int(input("Please enter your first number"))
y=int(input("Please enter your second number"))
result = perform_calculation(x, y)
print("Addition:", result[0])
print("Subtraction:", result[1])
