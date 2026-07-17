import connection as database

def displayReport(sql, params=None):

    cursor = database.connect.cursor(dictionary=True)

    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)

    table = cursor.fetchall()
    cursor.close()

    if len(table) == 0:
        print("\nNo Records Found")
        return

    columns = list(table[0].keys())

    col_width = {}

    for col in columns:
        max_len = max(len(str(row[col])) for row in table)
        col_width[col] = max(max_len, len(col))

    print()

    header = " | ".join(f"{col:<{col_width[col]}}" for col in columns)
    print(header)
    print("-" * len(header))

    for row in table:
        print(" | ".join(f"{str(row[col]):<{col_width[col]}}" for col in columns))

    print()


# --------------------------------------------------------
# Month Wise Income Expense Report
# --------------------------------------------------------

def MonthWiseIncomeExpenseReport():

    month = input("Enter Month (1-12): ")
    year = input("Enter Year : ")

    sql = "SELECT CASE WHEN flag=1 THEN 'Income' WHEN flag=2 THEN 'Expense' END AS Type, SUM(amount) AS Total_Amount FROM `transaction` WHERE is_deleted=0 AND MONTH(trandate)=%s AND YEAR(trandate)=%s GROUP BY flag"
   

    displayReport(sql, (month, year))


# --------------------------------------------------------
# Quarter Wise Income Expense Report
# --------------------------------------------------------

def QuarterWiseIncomeExpenseReport():

    quarter = int(input("Enter Quarter (1-4): "))
    year = input("Enter Year : ")

    if quarter == 1:
        start = 1
        end = 3
    elif quarter == 2:
        start = 4
        end = 6
    elif quarter == 3:
        start = 7
        end = 9
    else:
        start = 10
        end = 12

    sql = "SELECT CASE WHEN flag=1 THEN 'Income' WHEN flag=2 THEN 'Expense' END AS Type, SUM(amount) AS Total_Amount FROM `transaction` WHERE is_deleted=0 AND MONTH(trandate) BETWEEN %s AND %s AND YEAR(trandate)=%s GROUP BY flag"
  

    displayReport(sql, (start, end, year))


# --------------------------------------------------------
# Year Wise Income Expense Report
# --------------------------------------------------------

def YearWiseIncomeExpenseReport():

    year = input("Enter Year : ")

    sql = "SELECT CASE WHEN flag=1 THEN 'Income' WHEN flag=2 THEN 'Expense' END AS Type, SUM(amount) AS Total_Amount FROM `transaction` WHERE is_deleted=0 AND YEAR(trandate)=%s GROUP BY flag"
   

    displayReport(sql, (year,))


# --------------------------------------------------------
# Tour Wise Income Expense Report
# --------------------------------------------------------

def TourWiseIncomeExpenseReport():

    tourid = input("Enter Tour ID : ")

    sql = "SELECT CASE WHEN flag=1 THEN 'Income' WHEN flag=2 THEN 'Expense' END AS Type, SUM(amount) AS Total_Amount FROM `transaction` WHERE is_deleted=0 AND tourid=%s GROUP BY flag"
    

    displayReport(sql, (tourid,))


# --------------------------------------------------------
# All Tour Income Expense Report
# --------------------------------------------------------

def AllTourIncomeExpenseReport():

    sql = "SELECT tourid, SUM(CASE WHEN flag=1 THEN amount ELSE 0 END) AS Total_Income, SUM(CASE WHEN flag=2 THEN amount ELSE 0 END) AS Total_Expense, SUM(CASE WHEN flag=1 THEN amount ELSE -amount END) AS Profit FROM `transaction` WHERE is_deleted=0 GROUP BY tourid ORDER BY tourid"
    displayReport(sql)