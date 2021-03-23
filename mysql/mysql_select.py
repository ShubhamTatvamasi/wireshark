import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database="classicmodels"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
