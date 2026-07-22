import connection as database
from mysql.connector import Error as MySQLError


def InsertLecture():
    cursor = database.connect.cursor(dictionary=True)

    try:
        teacherid = int(input("Enter Teacher ID: "))
        subjectid = int(input("Enter Subject ID: "))
        batchid = int(input("Enter Batch ID: "))
        duration = int(input("Enter Lecture Duration (in minutes): "))
        lecturedate = input("Enter Lecture Date (YYYY-MM-DD): ")
        cursor.execute("SELECT per_hour_rate FROM subject WHERE id = %s AND is_deleted = 0", (subjectid,))
        subject_row = cursor.fetchone()

        if not subject_row:
            print("\n[-] Invalid Subject ID or Subject is deleted. Cannot insert lecture.\n")
            return

        per_hour_rate = subject_row['per_hour_rate']
        amount = (duration / 60) * float(per_hour_rate)

        sql = """
            INSERT INTO lecture (teacherid, subjectid, batchid, duration_in_minutes, amount, lecturedate, paymentid) 
            VALUES (%s, %s, %s, %s, %s, %s, 0)
        """
        values = [teacherid, subjectid, batchid, duration, amount, lecturedate]

        # Execute અને Commit
        cursor.execute(sql, values)
        database.connect.commit()

        print(f"\n[+] Lecture inserted successfully! Calculated Amount: {amount:.2f}\n")

    except ValueError:
        print("\n[-] Error: Teacher ID, Subject ID, Batch ID અને Duration ફક્ત નંબર જ હોવા જોઈએ.\n")
    except MySQLError as err:
        database.connect.rollback()
        print(f"\n[-] Database Error: {err}\n")
    finally:
        cursor.close()


def SelectLecture():
    cursor = database.connect.cursor(dictionary=True)

    try:
        sql = """
            SELECT l.id, t.name AS teacher_name, s.title AS subject_title, l.batchid, 
                   l.duration_in_minutes, l.amount, l.lecturedate 
            FROM lecture l
            INNER JOIN teacher t ON l.teacherid = t.id
            INNER JOIN subject s ON l.subjectid = s.id
            ORDER BY l.id DESC
        """
        cursor.execute(sql)
        table = cursor.fetchall()

        if not table:
            print("\n[-] No lecture records found.\n")
            return

        print(f"\n{'ID':<5} {'Teacher Name':<20} {'Subject Title':<25} {'Batch ID':<10} {'Duration':<10} {'Amount':<10} {'Date':<12}")
        print("-" * 97)

        count = 0
        for row in table:
            print(f"{row['id']:<5} {row['teacher_name']:<20} {row['subject_title']:<25} {row['batchid']:<10} {row['duration_in_minutes']:<10} {row['amount']:<10.2f} {str(row['lecturedate']):<12}")
            count += 1
            if count == 25:
                input("\nPress Enter to continue viewing...")
                count = 0
        print()

    except MySQLError as err:
        print(f"\n[-] Database Error: {err}\n")
    finally:
        cursor.close()