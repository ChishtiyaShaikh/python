n=input("Enter range end from 1 to :")
n=int(n)
for i in range(1 , n):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("fizz")
    elif i % 3 == 0:
        print("Buzz")
    else :
        print(i)  