def addition(num1,num2):
    print(f"AdditioN of {num1} and {num2} is",round(int(num1)+int(num2)))

def sub(num1,num2):
    print(f"Subtraction of {num1} and {num2} is", round(int(num1)-int(num2)))

def mult(num1,num2):
    print(f"multipication of {num1} and {num2} is", round(int(num1)*int(num2)))

def div(num1,num2):
    print(f"division of {num1} and {num2} is", round(int(num1)/int(num2)))

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
option = input("Choose n option from (+ , - , * , /):")

if option == '+':
    addition(num1,num2)
elif option == '-':
    sub(num1,num2)
elif option == '*':
    mult(num1,num2)
elif option == '/':
    div(num1,num2)
else:
    print("Invalid input")