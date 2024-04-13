import mysql.connector as sq
s = sq.connect(host="localhost", user="root", passwd="Chish@2005", database="Registration")
if s.is_connected():
    print("Hello! Welcome to Python-MySQL connectivity")
