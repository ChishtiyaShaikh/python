num1=input("Enter first number: ")
num2=input("Enter second number: ")


# when we take an input from a user it always take it as a string
# eg...
print("addition of " + num1 + " and " + num2 + " is ", num1 + num2)

# so it will concatenate two numbers as a string

# to avoid that we have to concatenate the input as a integer
# eg...
print("addition of " + num1 + " and " + num2 + " is ", int(num1) + int(num2))
 