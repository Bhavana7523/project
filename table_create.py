import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Bhavana@7523",database = "Inventory_Management")
cur=mydb.cursor()
manufacture_table='create table manufacture(manufacture_id integer(5) primary key,manufacture_date date,item_name varchar(30),no_of_items integer(5),defective_items integer(5),item_color varchar(20),company varchar(30))'
goods_table="create table goods(goods_id integer(5) primary key,manufacture_id integer(5),item_name varchar(30),item_color varchar(20),item_price integer(5),manufactured_date date)"
purchase_table='create table purchase (purchase_id integer(5) primary key,goods_id integer(5),purchase_date date,purchase_amount integer(5),purchase_store varchar(50))'
sales_table='create table sales(sale_id integer(5) primary key,goods_id integer(5),sale_date date,sale_amount integer(5),sale_store varchar(50),profit_margin integer(5))'
cur.execute(manufacture_table)
cur.execute(goods_table)
cur.execute(purchase_table)
cur.execute(sales_table)
