import mysql.connector
connection = mysql.connector.connect( host="localhost", user="root",
password="123456", database="bancoPython")
cursor = connection.cursor()

delete = "delete from Artists where name = 'Joao';"

cursor.execute(delete)

connection.commit()
connection.close()