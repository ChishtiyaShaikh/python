

Prasad={'Name':'Prasad Gadekar','PRN-NO':375,'Pointers':8.60}
Rahul={'Name':'Rahul Mandal','PRN-NO':373,'Pointers':7.60}
Chishtiya={'Name':'Chishtiya Shaikh','PRN-NO':375,'Pointers':8.30}

choose = input("enter student name: ")

if choose=='prasad':
    choose_2 = input("Enter the information you want (Name, PRN, Result): ")
    if choose_2=='Name':
        print(Prasad['Name'])
    elif choose_2 == 'PRN':
        print(Prasad['PRN'])
    elif choose_2 == 'Result':
        print(Prasad['Pointers'])
elif choose=='Rahul':
    choose_2 = input("Enter the information you want (Name, PRN, Result): ")
    if choose_2=='Name':
        print(Rahul['Name'])
    elif choose_2 == 'PRN':
        print(Rahul['PRN'])
    elif choose_2 == 'Result':
        print(Rahul['Pointers'])
elif choose=='Chishtiya':
    choose_2 = input("Enter the information you want (Name, PRN, Result): ")
    if choose_2=='Name':
        print(Chishtiya['Name'])
    elif choose_2 == 'PRN':
        print(Chishtiya['PRN'])
    elif choose_2 == 'Result':
        print(Chishtiya['Pointers'])