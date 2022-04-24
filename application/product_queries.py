import mysql.connector
# need to install following packages: mysql-connector, mysql-connector-python, mysql-connector-python-rf

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="lotr_shop"
)

# print(mydb)

# # Test query
# mycursor = mydb.cursor()
# mycursor.execute("SELECT size FROM size WHERE size = 's'")
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)

