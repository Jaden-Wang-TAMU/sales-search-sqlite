import sqlite3

_conn = sqlite3.connect('sales.sqlite')
<<<<<<< HEAD
result = _conn.execute("SELECT amount, first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='Tools'")
=======
result = _conn.execute("SELECT amount, first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='Baby'")
>>>>>>> refs/remotes/origin/master

# result = _conn.execute("SELECT amount, last_name, first_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='Baby'")

row=result.fetchall()
sale_list=[]
for each in row:
    # last_name=each[2]
    # command="SELECT sum(amount), first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE last_name='"+last_name+"'"
    # print(command)
    first_name=each[1]
    second_name=each[2]
    
<<<<<<< HEAD
    command='SELECT sum(amount), first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department="Tools" and first_name="'+first_name+'" and last_name="'+second_name+'"'
=======
    command="SELECT sum(amount), first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='Baby' and first_name='"+first_name+"'"+" and last_name='"+second_name+"'"
>>>>>>> refs/remotes/origin/master
    # This doesn't work

    # command="SELECT sum(amount), first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='Baby' and first_name='"+first_name+"'"+" and last_name='"+"Lazare"+"'"
    # This works, with last_name as a literal string, no each[2]

    # command="SELECT sum(amount), first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE last_name='"+second_name+"'"
    # This doesn't work, with second_name being a string and equal to each[2]

    # command="SELECT sum(amount), last_name, first_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='Baby' and last_name='"+each[1]+"'"
    # This doesn't work, with flipping last_name and first_name's order in the original execution line and in this execution line. index 2 is not the problem, the data in each[2] is the problem
    
    sale_result = _conn.execute(command)
    sale_row=sale_result.fetchone()
    sale_list.append(sale_row)
<<<<<<< HEAD


final_result=[]
for x in range(100):
    maxSale=0
    maxRow=sale_list[0]
    for each in sale_list:
        roundCurrent=0
        roundCurrent=round(each[0], 2)
        if roundCurrent>maxSale and not final_result.__contains__(each):
                maxSale=roundCurrent
                maxRow=each
        elif roundCurrent==maxSale and not final_result.__contains__(each) and each[1]<maxRow[1]:
            maxSale=roundCurrent
            maxRow=each         
    final_result.append(maxRow)

final_optimization=[]
for each in final_result:
    rounded=round(each[0], 2)
    opt_tuple=(each[1], each[2], rounded)
    final_optimization.append(opt_tuple)
print(final_optimization)
=======
print(sale_list)


# final_result=[]
# for x in range(10):
#     maxSale=0
#     maxRow=sale_list[0]
#     for each in sale_list:
#         if each[0]>maxSale and not final_result.__contains__(each):
#             maxSale=each[0]
#             maxRow=each
#     final_result.append(maxRow)

# final_optimization=[]
# for each in final_result:
#     rounded=round(each[0], 2)
#     opt_tuple=(each[1], each[2], rounded)
#     final_optimization.append(opt_tuple)
# print(final_optimization)
            
    # current=round(sale_row[0], 2)
    # if(current>maxSale):
    #     maxSale=current
    #     maxID=each[0]
    # final_result = _conn.execute("SELECT first_name, last_name from buyers\n\tWHERE id='"+str(maxID)+"'")
    # final_row=final_result.fetchone()
>>>>>>> refs/remotes/origin/master

# def biggest_spenders(self, how_many, department):
#     """
#     Returns the how_many highest spenders in a specific department
#     """
#     return None
