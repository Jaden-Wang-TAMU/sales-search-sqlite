import sqlite3

# _conn = sqlite3.connect('sales.sqlite')
# result = _conn.execute("SELECT SUM(amount) FROM sales\n\tWHERE department='Electronics' and sale_date='2020-09-15'")
# row=result.fetchone()
# if row[0]!=None:
#     print(round(row[0], 2))
# else:
#     print(0)

# _conn = sqlite3.connect('sales.sqlite')
# result = _conn.execute("SELECT SUM(amount) FROM sales\n\tWHERE department='Music' and sale_date='2020-09-30'")
# row=result.fetchone()
# if row[0]!=None:
#     print(round(row[0], 2))
# else:
#     print(0)

# _conn = sqlite3.connect('sales.sqlite')
# result = _conn.execute("SELECT SUM(amount) FROM sales JOIN buyers ON buyers.id=sales.buyer_id\n\tWHERE sale_date>='2020-09-15' and sale_date<='2020-09-17' and country='Russia'")
# row=result.fetchone()
# if row[0]!=None:
#     print(round(row[0], 2))
# else:
#     print(0)

# _conn = sqlite3.connect('sales.sqlite')
# result = _conn.execute("SELECT SUM(amount) from sales\n\tWHERE buyer_id='799'")
# row=result.fetchone()
# if row[0]!=None:
#     print(round(row[0], 2))
# else:
#     print(0)

_conn = sqlite3.connect('sales.sqlite')
result = _conn.execute("SELECT buyer_id from sales")
row=result.fetchall()
maxSale=0
maxID=0
for each in row:
    sale_result = _conn.execute("SELECT SUM(amount) from sales\n\tWHERE buyer_id='"+str(each[0])+"'")
    sale_row=sale_result.fetchone()
    current=round(sale_row[0], 2)
    if(current>maxSale):
        maxSale=current
        maxID=each[0]
print(maxID)
final_result = _conn.execute("SELECT first_name, last_name from buyers\n\tWHERE id='"+str(maxID)+"'")
final_row=final_result.fetchone()
print(final_row)
# sale_result = _conn.execute("SELECT SUM(amount) from sales\n\tWHERE buyer_id=423")
# sale_row=sale_result.fetchone()
# print(round(sale_row[0], 2))

# sale_result = _conn.execute("SELECT SUM(amount) from sales\n\tWHERE buyer_id=392")
# sale_row=sale_result.fetchone()
# print(round(sale_row[0], 2))

_conn = sqlite3.connect('sales.sqlite')
result = _conn.execute("SELECT amount, first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='"+department+"'")
row=result.fetchall()