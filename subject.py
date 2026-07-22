import connection as database
from mysql.connector import Error as MySQLError


def InsertSubject():
    sql = "INSERT INTO subject (title, courseid, per_hour_rate, is_deleted) VALUES (%s, %s, %s, 0)"

    try:
        title = input("Enter Subject title: ")
        courseid = int(input("Enter Associated Course ID: "))
        per_hour_rate = float(input("Enter Per Hour Rate: "))

        values = [title, courseid, per_hour_rate]

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, values)
            database.connect.commit()
            print("\n[+] Subject inserted successfully!\n")
        finally:
            cursor.close()

    except ValueError:
        print("\n[-] Error: Course ID અને Per Hour Rate શુદ્ધ નંબર જ હોવા જોઈએ.\n")
    except MySQLError as err:
        database.connect.rollback()
        print(f"\n[-] Database Error: {err}\n")


def UpdateSubject():
    sql = "UPDATE subject SET title=%s, courseid=%s, per_hour_rate=%s WHERE id=%s AND is_deleted=0"

    try:
        sub_id = int(input("Enter Subject ID to update: "))
        title = input("Enter New Subject title: ")
        courseid = int(input("Enter New Associated Course ID: "))
        per_hour_rate = float(input("Enter New Per Hour Rate: "))

        values = [title, courseid, per_hour_rate, sub_id]

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, values)
            database.connect.commit()

            if cursor.rowcount != 0:
                print("\n[+] Subject updated successfully!\n")
            else:
                print("\n[-] Subject not found or already deleted.\n")
        finally:
            cursor.close()

    except ValueError:
        print("\n[-] Error: Subject ID, Course ID અને Rate માટે ફક્ત નંબર જ નાખો.\n")
    except MySQLError as err:
        database.connect.rollback()
        print(f"\n[-] Database Error: {err}\n")


def DeleteSubject():
    # is_deleted=0 ઉમેર્યું છે
    sql = "UPDATE subject SET is_deleted=1 WHERE id=%s AND is_deleted=0"

    try:
        sub_id = int(input("Enter Subject ID to delete: "))

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, [sub_id])
            database.connect.commit()

            if cursor.rowcount != 0:
                print("\n[+] Subject deleted successfully.\n")
            else:
                print("\n[-] Subject not found or already deleted.\n")
        finally:
            cursor.close()

    except ValueError:
        print("\n[-] Error: Subject ID ફક્ત નંબર જ હોવો જોઈએ.\n")
    except MySQLError as err:
        database.connect.rollback()
        print(f"\n[-] Database Error: {err}\n")


def SelectSubject():
    sql = "SELECT id, title, courseid, per_hour_rate FROM subject WHERE is_deleted = 0 ORDER BY id DESC"

    cursor = database.connect.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        table = cursor.fetchall()

        if not table:
            print("\n[-] No active subjects found.\n")
            return

        print(f"\n{'ID':<5} {'Subject Title':<30} {'Course ID':<12} {'Rate/Hour':<10}")
        print("-" * 62)

        count = 0
        for row in table:
            print(f"{row['id']:<5} {row['title']:<30} {row['courseid']:<12} {float(row['per_hour_rate']):<10.2f}")

            count += 1
            if count == 25:
                input("\nPress any key to continue...")
                count = 0
        print()
    except MySQLError as err:
        print(f"\n[-] Database Error: {err}\n")
    finally:
        cursor.close()


def SearchSubject():
    search_title = input("Enter Subject title to search: ")

    sql = "SELECT id, title, courseid, per_hour_rate FROM subject WHERE is_deleted = 0 AND title LIKE %s ORDER BY id DESC"

    cursor = database.connect.cursor(dictionary=True)
    try:
        cursor.execute(sql, (f"%{search_title}%",))
        table = cursor.fetchall()

        if not table:
            print("\n[-] No subject records found matching that name.\n")
            return

        print(f"\n{'ID':<5} {'Subject Title':<30} {'Course ID':<12} {'Rate/Hour':<10}")
        print("-" * 62)

        count = 0
        for row in table:
            print(f"{row['id']:<5} {row['title']:<30} {row['courseid']:<12} {float(row['per_hour_rate']):<10.2f}")

            count += 1
            if count == 25:
                input("\nPress any key to continue...")
                count = 0
        print()
    except MySQLError as err:
        print(f"\n[-] Database Error: {err}\n")
    finally:
        cursor.close()