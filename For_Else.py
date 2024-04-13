li = [10,30,50,70,80] 

for i in li :
    print(i)
# this statement will execute when it traverse successfully throughout the complete list
# in case loop has been fail to complete the traversal it will npt be execute
else :
    print("Loop traverse successfully")
    
print("----------------------------")
    
# in this scenario we have added a condition to break the loop so it will not traverse through the complete list
# which cause to not execute the else statement
    
li = [10,30,50,70,80] 

for i in li :
    if i==50 :
        print("Terminated successfully")
        break
    print(i)
else :
    print("Loop traverse successfully")