import connection as database

def InsertSubject():
    # create sql statement
    sql = "INSERT INTO subject (title, courseid, per_hour_rate) VALUES (%s, %s, %s)"

    # accept input from user 
    title = input("Enter Subject title: ")
    courseid = int(input("Enter Associated Course ID: "))
    per_hour_rate = int(input("Enter Per Hour Rate: "))

    # create list whose size must be equal to total placeholder 
    values = [title, courseid, per_hour_rate]
    
    # create cursor 
    cursor = database.connect.cursor()

    # run sql statement 
    cursor.execute(sql, values)

    # save changes 
    database.connect.commit()

    print("\n[+] Subject inserted successfully!\n")

def UpdateSubject():
    sql = "UPDATE subject SET title=%s, courseid=%s, per_hour_rate=%s WHERE id=%s AND is_deleted=0"

    # accept input from user 
    id = int(input("Enter Subject ID to update: "))
    title = input("Enter New Subject title: ")
    courseid = int(input("Enter New Associated Course ID: "))
    per_hour_rate = int(input("Enter New Per Hour Rate: "))

    
    values = [title, courseid, per_hour_rate, id]

    # create cursor 
    cursor = database.connect.cursor()

    # execute sql 
    cursor.execute(sql, values)

    # save changes 
    database.connect.commit()
    
    if cursor.rowcount != 0:
        print("\n[+] Subject updated successfully!\n")
    else:
        print("\n[-] Subject not found or already deleted.\n")

def DeleteSubject():
    # create sql statement
    sql = "UPDATE subject SET is_deleted=1 WHERE id=%s"

    # accept input
    id = int(input("Enter Subject ID to delete: "))

    # create list
    values = [id]

    # create cursor
    cursor = database.connect.cursor()

    # run sql command
    cursor.execute(sql, values)

    # save changes
    database.connect.commit()

    if cursor.rowcount != 0:
        print("\n[+] Subject deleted successfully.\n")
    else:
        print("\n[-] Subject not found.\n")

def SelectSubject():
    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    
    sql = "SELECT id, title, courseid, per_hour_rate FROM subject WHERE is_deleted = 0 ORDER BY id DESC"
    cursor.execute(sql)

    
    table = cursor.fetchall()

    if not table:
        print("\n[-] No active subjects found.\n")
        return

    
    print(f"\n{'ID':<5} {'Subject Title':<30} {'Course ID':<12} {'Rate/Hour':<10}")
    print("-" * 62)

    count = 0

    for row in table:
        print(f"{row['id']:<5} {row['title']:<30} {row['courseid']:<12} {row['per_hour_rate']:<10}")

        count += 1

        if count == 25:
            input("\nPress any key to continue...")
            count = 0
    print()

def SearchSubject():
    # accept input to search by subject name
    search_title = input("Enter Subject title to search: ")

    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    
    sql = "SELECT id, title, courseid, per_hour_rate FROM subject WHERE is_deleted = 0 AND title LIKE %s ORDER BY id DESC"
    
    # execute with placeholder value
    cursor.execute(sql, (f"%{search_title}%",))

    # fetch and display all rows
    table = cursor.fetchall()

    if not table:
        print("\n[-] No subject records found matching that name.\n")
        return

    
    print(f"\n{'ID':<5} {'Subject Title':<30} {'Course ID':<12} {'Rate/Hour':<10}")
    print("-" * 62)

    count = 0

    for row in table:
        print(f"{row['id']:<5} {row['title']:<30} {row['courseid']:<12} {row['per_hour_rate']:<10}")

        count += 1

        if count == 25:
            input("\nPress any key to continue...")
            count = 0
    print()

      