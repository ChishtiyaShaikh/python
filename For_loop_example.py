height=input("Enter list members separated by space: ")

height_li=height.split()
count=0
for i in height_li:
    count=count+1
for i in range(count):
    height_li[i]=int(height_li[i]) # type: ignore
print(height_li)

total=0
for i in height_li:
    total+=i # type: ignore
avg=total/count
print(avg)
