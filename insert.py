t1='insert into manufacture(manufacture_id,manufacture_date,item_name,no_of_items,defective_items,item_color,company) values(%s,%s,%s,%s,%s,%s,%s)'
a=[(1, '2023-04-01', 'Shirt', 1000, 30,'Red','SS Exports'),
   (2, '2023-04-02', 'Toy Car', 600, 20,'Red','VR Exports'),
      (3, '2023-04-01', 'Toy Car',  850, 35,'Yellow','RR Exports'),
      (4, '2023-04-02', 'Wooden Chair', 200, 15,'Orange','SS Exports'),
      (5, '2023-04-03', 'Wooden Table', 150, 12,'White','SS Exports'),
      (6,'2023-04-04','Bottle',1500,40,'Black','RR Exports')]
cur.executemany(t1,a)
print("manufacture inserted successfully")
t2='insert into goods(goods_id,manufacture_id,item_name,item_color,item_price,manufactured_date) values(%s,%s,%s,%s,%s,%s)'
b=[ (1, 1, 'Shirt', 'Red', 150, '2023-04-01'),
    (2, 2, 'Toy Car', 'Red', 200, '2023-04-02'),
    (3, 3, 'Toy Car', 'Yellow', 200, '2023-04-01'),
    (4, 4, 'Wooden Chair', 'Orange', 300, '2023-04-02'),  
    (5, 5, 'Wooden Table', 'White', 300, '2023-04-03'),
    (6,6,'Bottle','Black',100,'2023-04-04')]
cur.executemany(t2,b)
print("Goods inserted successfully")
t3='insert into purchase(purchase_id,goods_id,purchase_date,purchase_amount,purchase_store) values(%s,%s,%s,%s,%s)'
c=[ (1, 1, '2023-04-06', 26500, 'ORay'),
    (2, 2, '2023-04-07', 5600, 'MyKids'),
    (3, 3, '2023-04-08', 13050, 'LuckyStores'),
    (4, 4, '2023-04-09', 6500, 'V-mart'),
   (5, 5, '2023-04-10', 4750, 'More')]
cur.executemany(t3,c)
print("purchase inserted successfully")
t4='insert into sales(sale_id,goods_id,sale_date,sale_amount,sale_store,profit_margin) values(%s,%s,%s,%s,%s,%s)'
d=[(1, 1, '2023-04-16', 30000, 'MyCare', 5000),
    (2, 2, '2023-04-17', 9000, 'MyKids', 1500),
    (3, 3, '2023-04-18', 13500, 'LuckyStores', 2250),
    (4, 4, '2023-04-19', 6000, 'V-mart', 1000),
    (5, 5, '2023-04-20', 4500, 'More',750)]
cur.executemany(t4,d)
print("Sales inserted successfully") 
mydb.commit()
