import sqlite3

class Search:

    # _conn = sqlite3.connect('sales.sqlite')
    
    def department_total(self, dept):
        """
        Returns the sum of all sales within a department
        """
        _conn = sqlite3.connect('sales.sqlite')
        command="SELECT SUM(amount) FROM sales\n\tWHERE department='"+dept+"'"
        result = _conn.execute(command)
        row=result.fetchone()
        return round(row[0], 2)

    def department_total_bydate(self, dept, date):
        """
        Returns the sum of all sales within a department on a specific date
        """
        _conn = sqlite3.connect('sales.sqlite')
        command="SELECT SUM(amount) FROM sales\n\tWHERE department='"+dept+"' and sale_date='"+date+"'"
        result = _conn.execute(command)
        row=result.fetchone()
        if row[0]!=None:
            return(round(row[0], 2))
        else:
            return(0)


    def country_count_date_range(self, country, start_date, end_date):
        """
        Returns the number of sales to buyers in a specific country between 2 dates, inclusive
        """
        _conn = sqlite3.connect('sales.sqlite')
        command="SELECT SUM(amount) FROM sales JOIN buyers ON buyers.id=sales.buyer_id\n\tWHERE sale_date>='"+start_date+"' and sale_date<='"+end_date+"' and country='"+country+"'"
        result = _conn.execute(command)
        row=result.fetchone()
        if row[0]!=None:
            return(round(row[0], 2))
        else:
            return(0)

    def biggest_spender(self):
        """
        Returns a tuple with the first and last name of the buyer who spent the most money
        """
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
        final_result = _conn.execute("SELECT first_name, last_name from buyers\n\tWHERE id='"+str(maxID)+"'")
        final_row=final_result.fetchone()
        return(final_row)

    def biggest_spenders(self, how_many, department):
        """
        Returns the how_many highest spenders in a specific department
        """
        _conn = sqlite3.connect('sales.sqlite')
        result = _conn.execute("SELECT amount, first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='"+department+"'")
        row=result.fetchall()
        sale_list=[]
        for each in row:
<<<<<<< HEAD
            sale_result = _conn.execute('SELECT sum(amount), first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department="'+department+'" and first_name="'+each[1]+'" and last_name="'+each[2]+'"')
=======
            sale_result = _conn.execute("SELECT sum(amount), first_name, last_name FROM sales JOIN buyers ON sales.buyer_id=buyers.id\n\tWHERE department='"+department+"' and first_name='"+each[1]+"'"+" and last_name='"+each[2]+"'")
>>>>>>> refs/remotes/origin/master
            sale_row=sale_result.fetchone()
            sale_list.append(sale_row)
        final_result=[]
        for x in range(how_many):
            maxSale=0
            maxRow=sale_list[0]
            for each in sale_list:
<<<<<<< HEAD
                roundCurrent=0
                roundCurrent=round(each[0], 2)
                if roundCurrent>maxSale and not final_result.__contains__(each):
                    maxSale=roundCurrent
                    maxRow=each
                elif roundCurrent==maxSale and not final_result.__contains__(each) and each[1]<maxRow[1]:
                    maxSale=roundCurrent
=======
                if each[0]>maxSale and not final_result.__contains__(each):
                    maxSale=each[0]
>>>>>>> refs/remotes/origin/master
                    maxRow=each
            final_result.append(maxRow)

        final_optimization=[]
        for each in final_result:
            rounded=round(each[0], 2)
            opt_tuple=(each[1], each[2], rounded)
            final_optimization.append(opt_tuple)
<<<<<<< HEAD
        return(final_optimization)
=======
        return(final_optimization)
>>>>>>> refs/remotes/origin/master
