# need to install following packages: mysql-connector, mysql-connector-python, mysql-connector-python-rf
# mysql.connector allows us to communicate with mysql through python
import mysql.connector


# this block of code creates a database instance and connects to the correct database on mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    # add password if you have one, have empty quote marks if you don't
    database="lotr_shop"
)

# this is to check you have successfully connected to the database
# print(mydb)

# # Test query
# mycursor = mydb.cursor()
# mycursor.execute("SELECT size FROM size WHERE size = 's'")
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)

