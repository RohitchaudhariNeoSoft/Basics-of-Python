## pip install mysql-connector
import mysql.connector

my_db = mysql.connector.connect(host="localhost",user = "rohit", password="1234")   ##credential to establish connection

mycursor = my_db.cursor()   ## Essential to fetch data

mycursor.execute("Show databases")  ## Mysql commands 