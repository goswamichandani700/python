import connection as database
import tour as t

def AddTransaction():
    t.Viewtour()

    # Accept input from user
    tourid = input("Enter Tour ID : ")
    amount = float(input("Enter Amount : "))

   
    flag = input("Enter Flag (1=Income, 2=Expense) : ")

    description = input("Enter Description : ")
    challanno = input("Enter Challan No : ")
    trandate = input("Enter Transaction Date (YYYY-MM-DD) : ")

    # Create SQL statement
    sql =  " INSERT INTO `transaction`(tourid, amount, flag, description, challanno, trandate, is_deleted)VALUES (%s,%s,%s,%s,%s,%s,%s)"

    # Create values list
    values = [tourid,amount,flag,description,challanno,trandate,0]

    # Create cursor
    cursor = database.connect.cursor()

    # Execute SQL statement
    cursor.execute(sql, values)

    # Save changes
    database.connect.commit()

    print("Transaction inserted successfully.")

    key = input("Press any key to continue")

def SearchTransaction():
    description = input("Enter Description : ")

    sql = """
    SELECT id,tourid,amount,flag,description,challanno,trandate
    FROM `transaction`
    WHERE description LIKE %s
    AND is_deleted = 0
    ORDER BY id
    """

    # Create cursor
    cursor = database.connect.cursor(dictionary=True)

    # Run SQL command
    cursor.execute(sql, (f"%{description}%",))

    # Fetch all records
    table = cursor.fetchall()

    if len(table) == 0:
        print("No Transaction Found")
    else:
        print(f"{'ID':<5} {'TourID':<8} {'Amount':<10} {'Type':<10} {'Description':<25} {'Challan':<12} {'Date':<12}")
        print("_"*100)

        for row in table:
             print(f"{row['id']:<5} {row['tourid']:<8} {row['amount']:<10} {row['flag']:<8} {row['description']:<25} {row['challanno']:<12} {str(row['trandate']):<12}")

        print("_"*100)

    input("Press any key to continue")
def DisplayTransaction():

    sql = """
    SELECT id, tourid, amount, flag, description, challanno, trandate
    FROM `transaction`
    WHERE is_deleted = 0
    ORDER BY id
    """

    # Create cursor
    cursor = database.connect.cursor(dictionary=True)

    # Run SQL command
    cursor.execute(sql)

    # Fetch all records
    table = cursor.fetchall()

    if len(table) == 0:
        print("No Transaction Found")
    else:
        print(f"{'ID':<5} {'Tour ID':<8} {'Amount':<10} {'Type':<10} {'Description':<30} {'Challan No':<15} {'Date':<12}")
        print("_"*110)

        TotalIncome = 0
        TotalExpense = 0

        for row in table:

            if row['flag'] == 1:
                type = "Income"
                TotalIncome += row['amount']
            else:
                type = "Expense"
                TotalExpense += row['amount']

            print(f"{row['id']:<5} {row['tourid']:<8} {row['amount']:<10} {type:<10} {row['description']:<30} {row['challanno']:<15} {str(row['trandate']):<12}")

        print("_"*110)
        print(f"Total Income : {TotalIncome}")
        print(f"Total Expense: {TotalExpense}")

    key = input("Press any key to continue...")   

def DeleteTransaction():
    DisplayTransaction()

    id = int(input("Enter Transaction ID to Delete : "))

    cursor = database.connect.cursor()

    sql1 = "SELECT COUNT(*) FROM `transaction` WHERE id = %s AND is_deleted = 0"
    cursor.execute(sql1, (id,))

    count = cursor.fetchone()[0]

    # print("Count =", count)

    if count == 0:
        print("Transaction ID Not Found")
    else:
        sql = "UPDATE `transaction` SET is_deleted = 1 WHERE id = %s"
        cursor.execute(sql, (id,))
        print("Rows Updated =", cursor.rowcount)
        database.connect.commit()
        print("Transaction Deleted Successfully")

    input("Press any key to continue...")


    
       


