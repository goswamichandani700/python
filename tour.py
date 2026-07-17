import connection as database 
def AddTour():
    sql = "insert into tour (title, detail, start_date, days, adult_rate, child_rate) values (%s,%s,%s,%s,%s,%s)"
    # %s is called placeholder 

    #accept input from user 
    title = input("Enter Tour Title : ")
    detail = input("Enter Tour Detail : ")
    start_date = input("Enter Start Date (YYYY-MM-DD) : ")
    days = int(input("Enter Number of Days : "))
    adult_rate = float(input("Enter Adult Rate : "))
    child_rate = float(input("Enter Child Rate : "))

    #create list whose size must be equal to total placeholder 
    values = [title, detail, start_date, days, adult_rate, child_rate]
    #create cursor 
    cursor = database.connect.cursor()

    #run sql statement 
    cursor.execute(sql,values)

    #save changes 
    database.connect.commit()

    print("Tour inserted successfully")
 
    
def ViewTour(SQLCommand=None, title=None):
    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    if SQLCommand == None:
        # create sql statement
        sql = "SELECT id, title, detail, start_date, days,adult_rate, child_rate FROM tour WHERE is_deleted = 0 ORDER BY id DESC"
        cursor.execute(sql)
    else:
        sql = SQLCommand
        cursor.execute(sql, (f"%{title}%",))

    # fetch and display all rows
    table = cursor.fetchall()

    print(f"{'ID':<5} {'Title':<25} {'Detail':<50} {'Start Date':<20} {'Days':<6} {'Adult Rate':<12} {'Child Rate':<12}")
    print("-" * 120)

    count = 0

    for row in table:
        print(f"{row['id']:<5} " f"{row['title']:<25} " f"{row['detail'][:50]:<50} " f"{str(row['start_date']):<20} " f"{row['days']:<6} "f"{row['adult_rate']:<12} "  f"{row['child_rate']:<12}")

        count += 1

        if count == 25:
            input("Press any key to continue...")
            count = 0

def DeleteTour():
    # create sql statement
    sql = "UPDATE tour SET is_deleted=1 WHERE id=%s"

    # accept input
    id = int(input("Enter Tour ID: "))

    # create list
    values = [id]

    # create cursor
    cursor = database.connect.cursor()

    # run sql command
    cursor.execute(sql, values)

    # save changes
    database.connect.commit()

    if cursor.rowcount != 0:
        print("Tour deleted successfully.")
    else:
        print("Tour not found.")
   

def UpdateTour():
        #create sql statement 
    sql = "update tour set title=%s,detail=%s,start_date=%s,days=%s,adult_rate=%s,child_rate=%s where id=%s"

    #accept input from user 
    id = int(input("enter product id"))
    title = input("Enter Tour Title : ")
    detail = input("Enter Tour Detail : ")
    start_date = input("Enter Start Date (YYYY-MM-DD HH:MM:SS) : ")
    days = int(input("Enter Number of Days : "))
    adult_rate = float(input("Enter Adult Rate : "))
    child_rate = float(input("Enter Child Rate : "))

    #create list 
    values = [title, detail, start_date, days, adult_rate, child_rate,id]

    #create cursor 
    cursor = database.connect.cursor()

    #execute sql 
    cursor.execute(sql,values)

    #save changes 
    database.connect.commit()
    if cursor.rowcount !=0:
        print("tour updated")
    else:
        print("tour not found")  

