import connection as database
from mysql.connector import Error as MySQLError


def InsertCourse():
    sql = "INSERT INTO course (title, description, duration, fees, is_deleted) VALUES (%s, %s, %s, %s, 0)"

    try:
        title = input("Enter Course Title : ")
        description = input("Enter Course description : ")
        duration = int(input("Enter Duration (in months) : "))
        fees = float(input("Enter Course Fees : "))

        values = [title, description, duration, fees]

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, values)
            database.connect.commit()
            print("Course inserted successfully.")
        finally:
            cursor.close()

    except ValueError:
        print("Error: Duration and Fees (only integer).")
    except MySQLError as err:
        database.connect.rollback()
        print(f"Database Error: {err}")


def UpdateCourse():
    sql = "UPDATE course SET title=%s, description=%s, duration=%s, fees=%s WHERE id=%s AND is_deleted=0"

    try:
        course_id = int(input("Enter Course ID to update : "))
        title = input("Enter Course Title : ")
        description = input("Enter Course description : ")
        duration = int(input("Enter Duration (in months) : "))
        fees = float(input("Enter Course Fees : "))

        values = [title, description, duration, fees, course_id]

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, values)
            database.connect.commit()

            if cursor.rowcount > 0:
                print("Course updated successfully.")
            else:
                print("Course not found or already deleted.")
        finally:
            cursor.close()

    except ValueError:
        print("Error: ID, Duration and Fees માટે ")
    except MySQLError as err:
        database.connect.rollback()
        print(f"Database Error: {err}")


def DeleteCourse():
    sql = "UPDATE course SET is_deleted=1 WHERE id=%s AND is_deleted=0"

    try:
        course_id = int(input("Enter Course ID: "))

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, (course_id,))
            database.connect.commit()

            if cursor.rowcount > 0:
                print("Course deleted successfully.")
            else:
                print("Course not found or already deleted.")
        finally:
            cursor.close()

    except ValueError:
        print("Error: Course ID (integer).")
    except MySQLError as err:
        database.connect.rollback()
        print(f"Database Error: {err}")


def SelectCourse():
    sql = "SELECT id, title, description, duration, fees FROM course WHERE is_deleted = 0 ORDER BY id DESC"

    cursor = database.connect.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        table = cursor.fetchall()

        if not table:
            print("No active courses found.")
            return

        print(f"{'ID':<5} {'Title':<25} {'Description':<40} {'Duration (Months)':<20} {'Fees':<12}")
        print("-" * 105)

        count = 0
        for row in table:
            print(f"{row['id']:<5} {row['title']:<25} {row['description'][:40]:<40} {row['duration']:<20} {row['fees']:<12.2f}")

            count += 1
            if count == 25:
                input("Press Enter to continue...")
                count = 0
    except MySQLError as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()


def SearchCourse():
    sql = "SELECT id, title, description, duration, fees FROM course WHERE is_deleted = 0 AND title LIKE %s ORDER BY id DESC"

    search_title = input("Enter Course Title to search: ")

    cursor = database.connect.cursor(dictionary=True)
    try:
        cursor.execute(sql, (f"%{search_title}%",))
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
                input("Press Enter to continue...")
                count = 0
    except MySQLError as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()