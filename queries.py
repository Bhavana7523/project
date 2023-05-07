# Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.
dele='DELETE FROM goods WHERE goods.goods_id in(SELECT goods_id from(SELECT goods.goods_id FROM goods JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id JOIN purchase ON goods.goods_id = purchase.goods_id WHERE goods.item_name = "Shirt" AND purchase.purchase_store = "ORay" AND manufacture.manufacture_date = "2023-04-01" AND manufacture.defective_items >0 limit 1)as c)'
 cur.execute(dele)
 print("Deleted successfully")
 mydb.commit()
# Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
 upd="UPDATE manufacture m JOIN goods g ON m.manufacture_id = g.manufacture_id JOIN purchase p ON g.goods_id = p.goods_id SET m.no_of_items = m.no_of_items + p.purchase_amount, m.defective_items = m.defective_items + (p.purchase_amount * 0.05) WHERE g.item_name = 'Toy Car' AND g.item_color = 'Red' AND p.purchase_store='MyKids'"
 cur.execute(upd)
 print("Updated successfully")
 mydb.commit()
# Display all the “wooden chair” items that were manufactured before the 1st May 2023. 
 display="SELECT * FROM goods WHERE item_name = 'Wooden Chair' AND manufactured_date < '2023-05-01'"
  cur.execute(display)
  print("Displayed Successfully")
 my_result2=cur.fetchall()
 for x in my_result2:
    print(x)
 mydb.commit()
# Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.
cur.execute("SELECT profit_margin FROM sales,goods, manufacture WHERE goods.goods_id = sales.goods_id AND goods.item_name = 'wooden table' AND manufacture.company = 'SS Export' AND sales.sale_store = 'MyCare'")
my_result2=cur.fetchall()
for i in my_result2:
    print(i)
mydb.commit()
