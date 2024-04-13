budget=int(input("Enter your budget: "))

if budget > 1000 and budget <= 5000:
    print("You can buy samsung guru")
elif budget > 5000 and budget <= 10000:
    print("You can buy redmi realme oppo or vivo")
elif budget > 10000 and budget <= 50000:
    print("You can buy Samsung mobile")
elif budget > 50000:
    print("You can buy an Iphone")
else :
    print("Increase your budget")