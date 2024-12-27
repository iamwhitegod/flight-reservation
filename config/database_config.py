# Rename to database_config.py for clarity
# import the connector

import mysql.connector

# establish connection to Mysql database


connection = mysql.connector.connect(
   host="localhost",
   user="root",
   password="z7fnvxQ2@",
   database="flight"
)

# create a cursor object to perform the queries

mycursor = connection.cursor()


# query for a table named users
# mycursor.execute("SELECT * FROM users")

mycursor.execute("SELECT user, host FROM mysql.user WHERE user = 'root';")

# fetch all retrieved rows

myresult = mycursor.fetchall()

# display all rows onto the console

for x in myresult:
  print(x)



mycursor.close()
connection.close()

def get_db_connection():
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="z7fnvxQ2@",
    database="flight"
  )
  return connection