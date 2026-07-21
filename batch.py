import connection as database

def InsertBatch():
    # create sql statement
    sql = "INSERT INTO batch (courseid, startdate, enddate, classtime, is_deleted) VALUES (%s, %s, %s, %s, 0)"

    # accept input from user
    courseid = int(input("Enter Course ID: "))
    startdate = input("Enter Start Date (YYYY-MM-DD): ")
    enddate = input("Enter End Date (YYYY-MM-DD): ")
    classtime = input("Enter Class Time (HH:MM:SS): ")

    # create list whose size must be equal to total placeholders
    values = [courseid, startdate, enddate, classtime]
    
    # create cursor
    cursor = database.connect.cursor()

    # run sql statement
    cursor.execute(sql, values)

    # save changes
    database.connect.commit()

    print("Batch inserted successfully")

def UpdateBatch():
    # create sql statement
    sql = "UPDATE batch SET courseid=%s, startdate=%s, enddate=%s, classtime=%s WHERE id=%s AND is_deleted=0"

    # accept input from user
    id = int(input("Enter Batch ID to update: "))
    courseid = int(input("Enter Course ID: "))
    startdate = input("Enter Start Date (YYYY-MM-DD): ")
    enddate = input("Enter End Date (YYYY-MM-DD): ")
    classtime = input("Enter Class Time (HH:MM:SS): ")

    # create list
    values = [courseid, startdate, enddate, classtime, id]

    # create cursor
    cursor = database.connect.cursor()

    # execute sql
    cursor.execute(sql, values)

    # save changes
    database.connect.commit()
    
    if cursor.rowcount != 0:
        print("Batch updated successfully")
    else:
        print("Batch not found or already deleted")

def DeleteBatch():
    # create sql statement
    sql = "UPDATE batch SET is_deleted=1 WHERE id=%s"

    # accept input
    id = int(input("Enter Batch ID: "))

    # create list
    values = [id]

    # create cursor
    cursor = database.connect.cursor()

    # run sql command
    cursor.execute(sql, values)

    # save changes
    database.connect.commit()

    if cursor.rowcount != 0:
        print("Batch deleted successfully.")
    else:
        print("Batch not found.")

def SelectBatch():
    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    # create sql statement
    sql = "SELECT id, courseid, startdate, enddate, classtime FROM batch WHERE is_deleted = 0 ORDER BY id DESC"
    cursor.execute(sql)

    # fetch and display all rows
    table = cursor.fetchall()

    if not table:
        print("No active batches found.")
        return

    print(f"{'ID':<5} {'Course ID':<12} {'Start Date':<15} {'End Date':<15} {'Class Time':<12}")
    print("-" * 65)

    count = 0

    for row in table:
        print(f"{row['id']:<5} {row['courseid']:<12} {str(row['startdate']):<15} {str(row['enddate']):<15} {str(row['classtime']):<12}")

        count += 1

        if count == 25:
            input("Press any key to continue...")
            count = 0

def SearchBatch():
    # accept input to search by course ID
    search_course_id = int(input("Enter Course ID to search associated batches: "))

    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    # create sql statement
    sql = "SELECT id, courseid, startdate, enddate, classtime FROM batch WHERE is_deleted = 0 AND courseid = %s ORDER BY id DESC"
    
    # execute with placeholder value
    cursor.execute(sql, (search_course_id,))

    # fetch and display all rows
    table = cursor.fetchall()

    if not table:
        print("No batch records found matching that Course ID.")
        return

    print(f"{'ID':<5} {'Course ID':<12} {'Start Date':<15} {'End Date':<15} {'Class Time':<12}")
    print("-" * 65)

    count = 0

    for row in table:
        print(f"{row['id']:<5} {row['courseid']:<12} {str(row['startdate']):<15} {str(row['enddate']):<15} {str(row['classtime']):<12}")

        count += 1

        if count == 25:
            input("Press any key to continue...")
            count = 0