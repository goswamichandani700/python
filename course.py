import connection as database 

def InsertCourse():
    sql = "insert into course (title, description, duration, fees) values (%s,%s,%s,%s)"

    # accept input from user 
    title = input("Enter Course Title : ")
    description = input("Enter Course description : ")
    duration = int(input("Enter Duration (in months) : "))
    fees = float(input("Enter Course Fees : "))

    # create list whose size must be equal to total placeholder 
    values = [title, description, duration, fees]
    
    # create cursor 
    cursor = database.connect.cursor()

    # run sql statement 
    cursor.execute(sql, values)

    # save changes 
    database.connect.commit()

    print("Course inserted successfully")

def UpdateCourse():
    # create sql statement 
    sql = "update course set title=%s, description=%s, duration=%s, fees=%s where id=%s"

    # accept input from user 
    id = int(input("Enter Course ID to update : "))
    title = input("Enter Course Title : ")
    description = input("Enter Course description : ")
    duration = int(input("Enter Duration (in months) : "))
    fees = float(input("Enter Course Fees : "))

    # create list 
    values = [title, description, duration, fees, id]

    # create cursor 
    cursor = database.connect.cursor()

    # execute sql 
    cursor.execute(sql, values)

    # save changes 
    database.connect.commit()
    
    if cursor.rowcount != 0:
        print("Course updated successfully")
    else:
        print("Course not found")

def DeleteCourse():
    # create sql statement
    sql = "UPDATE course SET is_deleted=1 WHERE id=%s"

    # accept input
    id = int(input("Enter Course ID: "))

    # create list
    values = [id]

    # create cursor
    cursor = database.connect.cursor()

    # run sql command
    cursor.execute(sql, values)

    # save changes
    database.connect.commit()

    if cursor.rowcount != 0:
        print("Course deleted successfully.")
    else:
        print("Course not found.")

def SelectCourse():
    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    # create sql statement
    sql = "SELECT id, title, description, duration, fees FROM course WHERE is_deleted = 0 ORDER BY id DESC"
    cursor.execute(sql)

    # fetch and display all rows
    table = cursor.fetchall()

    if not table:
        print("No courses found.")
        return

    print(f"{'ID':<5} {'Title':<25} {'Description':<40} {'Duration (Months)':<20} {'Fees':<12}")
    print("-" * 105)

    count = 0

    for row in table:
        print(f"{row['id']:<5} {row['title']:<25} {row['description'][:40]:<40} {row['duration']:<20} {row['fees']:<12.2f}")

        count += 1

        if count == 25:
            input("Press any key to continue...")
            count = 0

def SearchCourse():
    # accept input to search by course title
    search_title = input("Enter Course Title to search: ")

    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    # create sql statement using LIKE for partial matches
    sql = "SELECT id, title, description, duration, fees FROM course WHERE is_deleted = 0 AND title LIKE %s ORDER BY id DESC"
    
    # execute with placeholder value
    cursor.execute(sql, (f"%{search_title}%",))

    # fetch and display all rows
    table = cursor.fetchall()

    if not table:
        print("No course records found matching that title.")
        return

    print(f"{'ID':<5} {'Title':<25} {'Description':<40} {'Duration (Months)':<20} {'Fees':<12}")
    print("-" * 105)

    count = 0

    for row in table:
        print(f"{row['id']:<5} {row['title']:<25} {row['description'][:40]:<40} {row['duration']:<20} {row['fees']:<12.2f}")

        count += 1

        if count == 25:
            input("Press any key to continue...")
            count = 0