import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ritesh@63",
  database="sakila"
)

mycursor = mydb.cursor()


sql = "SELECT * FROM actor"
mycursor.execute(sql)


import csv

with open('customers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in mycursor.description])  # write header
    writer.writerows(mycursor)
