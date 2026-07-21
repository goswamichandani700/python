import connection as database

def InsertTeacher():
    
    sql = "INSERT INTO teacher (`name`, `mobile`, `email`, `gender`, `qualification`, `experience`) VALUES (%s,%s,%s,%s,%s,%s)"

    
    name = input("Enter Teacher Name: ")
    mobile = input("Enter Mobile Number: ")
    email = input("Enter Email Address: ")
    gender = input("Enter Gender (Male/Female): ")
    qualification = input("Enter Teacher Qualification: ")
    experience = int(input("Enter Teacher Experience (in years): "))

    
    values = [name, mobile, email, gender, qualification, experience]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()

    print("\n[+] Teacher record inserted successfully!\n")

def UpdateTeacher():
    sql = "UPDATE teacher SET name=%s, mobile=%s, email=%s, experience=%s WHERE id=%s AND is_deleted=0"

    id = int(input("Enter Teacher ID to update: "))
    name = input("Enter New Teacher Name: ")
    mobile = input("Enter New Mobile Number: ")
    email = input("Enter New Email Address: ")
    experience = int(input("Enter New Teacher Experience: "))

    
    values = [name, mobile, email, experience, id]

    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    
    if cursor.rowcount != 0:
        print("\n[+] Teacher record updated successfully!\n")
    else:
        print("\n[-] Teacher not found or already deleted.\n")

def DeleteTeacher():
    sql = "UPDATE teacher SET is_deleted=1 WHERE id=%s"
    id = int(input("Enter Teacher ID to delete: "))
    values = [id]

    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()

    if cursor.rowcount != 0:
        print("\n[+] Teacher marked as deleted successfully.\n")
    else:
        print("\n[-] Teacher record not found.\n")

def SelectTeacher():
    cursor = database.connect.cursor(dictionary=True)
    sql = "SELECT id, name, mobile, email, gender, qualification, experience FROM teacher WHERE is_deleted = 0 ORDER BY id DESC"
    cursor.execute(sql)
    table = cursor.fetchall()

    if not table:
        print("\n[-] No active teacher records found.\n")
        return

    
    print(f"\n{'ID':<5} {'Teacher Name':<20} {'Mobile':<13} {'Email':<25} {'Gender':<8} {'Qual.':<10} {'Exp':<5}")
    print("-" * 90)

    count = 0
    for row in table:
        print(f"{row['id']:<5} {row['name']:<20} {row['mobile']:<13} {row['email']:<25} {row['gender']:<8} {row['qualification']:<10} {row['experience']:<5}")
        count += 1
        if count == 25:
            input("\nPress any key to continue viewing...")
            count = 0
    print()

def SearchTeacher():
    search_name = input("Enter Teacher Name to search: ")
    cursor = database.connect.cursor(dictionary=True)

    
    sql = "SELECT id, name, mobile, email, gender, qualification, experience FROM teacher WHERE is_deleted = 0 AND name LIKE %s ORDER BY id DESC"
    cursor.execute(sql, (f"%{search_name}%",))
    table = cursor.fetchall()

    if not table:
        print("\n[-] No teacher records found matching that name.\n")
        return

    print(f"\n{'ID':<5} {'Teacher Name':<20} {'Mobile':<13} {'Email':<25} {'Gender':<8} {'Qual.':<10} {'Exp':<5}")
    print("-" * 90)

    count = 0
    for row in table:
        print(f"{row['id']:<5} {row['name']:<20} {row['mobile']:<13} {row['email']:<25} {row['gender']:<8} {row['qualification']:<10} {row['experience']:<5}")
        count += 1
        if count == 25:
            input("\nPress any key to continue...")
            count = 0
    print()