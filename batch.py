import connection as database
from mysql.connector import Error as MySQLError


def InsertBatch():
    sql = "INSERT INTO batch (courseid, startdate, enddate, classtime, is_deleted) VALUES (%s, %s, %s, %s, 0)"

    try:
        courseid = int(input("Enter Course ID: "))
        startdate = input("Enter Start Date (YYYY-MM-DD): ")
        enddate = input("Enter End Date (YYYY-MM-DD): ")
        classtime = input("Enter Class Time (HH:MM:SS): ")

        values = [courseid, startdate, enddate, classtime]

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, values)
            database.connect.commit()
            print("Batch inserted successfully.")
        finally:
            cursor.close()

    except ValueError:
        print("Error: Course ID શુદ્ધ નંબર (Integer) હોવો જોઈએ.")
    except MySQLError as err:
        database.connect.rollback()
        print(f"Database Error: {err}")


def UpdateBatch():
    sql = "UPDATE batch SET courseid=%s, startdate=%s, enddate=%s, classtime=%s WHERE id=%s AND is_deleted=0"

    try:
        batch_id = int(input("Enter Batch ID to update: "))
        courseid = int(input("Enter Course ID: "))
        startdate = input("Enter Start Date (YYYY-MM-DD): ")
        enddate = input("Enter End Date (YYYY-MM-DD): ")
        classtime = input("Enter Class Time (HH:MM:SS): ")

        values = [courseid, startdate, enddate, classtime, batch_id]

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, values)
            database.connect.commit()

            if cursor.rowcount > 0:
                print("Batch updated successfully.")
            else:
                print("Batch not found or already deleted.")
        finally:
            cursor.close()

    except ValueError:
        print("Error: Batch ID અને Course ID ફક્ત નંબર જ હોવા જોઈએ.")
    except MySQLError as err:
        database.connect.rollback()
        print(f"Database Error: {err}")


def DeleteBatch():
    # is_deleted=0 ચેક કરવું જરૂરી છે
    sql = "UPDATE batch SET is_deleted=1 WHERE id=%s AND is_deleted=0"

    try:
        batch_id = int(input("Enter Batch ID: "))

        cursor = database.connect.cursor()
        try:
            cursor.execute(sql, (batch_id,))
            database.connect.commit()

            if cursor.rowcount > 0:
                print("Batch deleted successfully.")
            else:
                print("Batch not found or already deleted.")
        finally:
            cursor.close()

    except ValueError:
        print("Error: Batch ID ફક્ત નંબર જ હોવો જોઈએ.")
    except MySQLError as err:
        database.connect.rollback()
        print(f"Database Error: {err}")


def SelectBatch():
    sql = "SELECT id, courseid, startdate, enddate, classtime FROM batch WHERE is_deleted = 0 ORDER BY id DESC"

    cursor = database.connect.cursor(dictionary=True)
    try:
        cursor.execute(sql)
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
                input("Press Enter to continue...")
                count = 0
    except MySQLError as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()


def SearchBatch():
    sql = "SELECT id, courseid, startdate, enddate, classtime FROM batch WHERE is_deleted = 0 AND courseid = %s ORDER BY id DESC"

    try:
        search_course_id = int(input("Enter Course ID to search associated batches: "))

        cursor = database.connect.cursor(dictionary=True)
        try:
            cursor.execute(sql, (search_course_id,))
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
                    input("Press Enter to continue...")
                    count = 0
        finally:
            cursor.close()

    except ValueError:
        print("Error: Course ID ફક્ત નંબર જ હોવો જોઈએ.")
    except MySQLError as err:
        print(f"Database Error: {err}")