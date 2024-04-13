
name="Prasad Gadekar"
length=len(name)
print(length)

# what if i want to write 
# ("Prasad Gadekar has" + length + "letters")
# print(name + " has " + length + "letters") 
# it will show error can only concatenate strings as length is int
# so the solution is typecasting like

print(name + " string has " + str(length) + " characters")

# in the same way we can convert anything from one data type to another data type like int(name), float(name), etc

num="10"

print(10 + int(num))

# here num stores 10 as an string in definition but later we typecast it with int so it is showing addition