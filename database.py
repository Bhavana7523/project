import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Bhavana@7523')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute('create database Inventory_Management')