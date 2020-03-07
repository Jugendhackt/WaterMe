import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="waterme"
)

print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO zeitverlauf (timestamp, data) VALUES (%s, %s)"
val = ("3456634", "blaaaaaaaaaaaaa")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")