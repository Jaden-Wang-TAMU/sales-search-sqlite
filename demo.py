# SELECT * FROM buyers;
# Gets all data

# ORDER BY last_name ASC;
# Reorders the database in ascending order for selected category

# ORDER BY last_name ASC, first_name ASC;
# Reorders in ascending order by last name first, and if same last name then order by first name

# WHERE country='China'
# shortens down database to just those who's country is in China

# JOIN sales
#    ON buyers.id=sales.buyer_id
# Takes every record from buyers and finds which sales belong to that buyer
# It can tell because both buyers and sales have the buyer ID variable, just under different names.

# ORDER BY last_name ASC, first_name ASC, sale_date DESC;
# Orders by name and then latest date

# SELECT first_name, last_name, email, department, amount, sale_date FROM buyers
# Gets specific categories from buyers

# GROUP BY buyer_id;
# No more than 1 record per unique buyer_id, but only gets first purchase

# SELECT first_name, last_name, email, department, SUM(amount) AS total, MIN(sale_date) as first_sale, MAX(sale_date) AS last_sale FROM buyers
# Gets you the total amout spent. Also gets first and last time they bought something.

import sqlite3

db=sqlite3.connect('sales.sqlite')

result = db.execute("SELECT * FROM buyers")

# while row=result.fetchone() # pulls the next record, basically an iterator
#     print(row) # Not that useful, wouldn't want to fetch one at a time
# result.fetchmany(10) # Fetches as many as you ask for

rows=result.fetchall() # gets everything as a matrix
for row in rows:
    print(row)

# There shouldn't be ifs or loops in this lab
# lots of group by, join, min, max, etc