import connection as database

def BatchWiseLectureDetails():
    cursor = None
    try:
        batchid = int(input("\nEnter Batch ID: "))
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")
        
        cursor = database.connect.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM batch WHERE id = %s AND is_deleted = 0", (batchid,))
        batch = cursor.fetchone()
        
        if not batch:
            print("\n[-] Active Batch ID not found.\n")
            return
            
        batch_title = batch.get('name') or batch.get('title') or f"Batch {batchid}"
        
        sql = """
            SELECT l.id, s.title AS subject_title, t.name AS teacher_name, 
                   l.duration_in_minutes, l.lecturedate
            FROM lecture l
            INNER JOIN subject s ON l.subjectid = s.id
            INNER JOIN teacher t ON l.teacherid = t.id
            WHERE l.batchid = %s AND l.lecturedate BETWEEN %s AND %s
            ORDER BY l.lecturedate ASC
        """
        cursor.execute(sql, (batchid, start_date, end_date))
        lectures = cursor.fetchall()
        
        if not lectures:
            print(f"\n[-] No lectures found for Batch '{batch_title}' between {start_date} and {end_date}.\n")
            return
            
        print(f"\n=========================================================================")
        print(f" LECTURE REPORT FOR BATCH: {batch_title} ({start_date} to {end_date})")
        print(f"=========================================================================")
        print(f"{'ID':<5} {'Subject Title':<22} {'Teacher Name':<20} {'Duration (Min)':<15} {'Date':<12}")
        print("-" * 75)
        
        total_duration = 0
        for row in lectures:
            print(f"{row['id']:<5} {row['subject_title']:<22} {row['teacher_name']:<20} {row['duration_in_minutes']:<15} {str(row['lecturedate']):<12}")
            total_duration += row['duration_in_minutes']
            
        print("-" * 75)
        print(f"Total Lectures: {len(lectures)} | Total Duration: {total_duration} Minutes\n")

    except Exception as e:
        print(f"\n[-] Error generating report: {e}\n")
    finally:
        if cursor:
            cursor.close()


def BatchWiseLectureWithTotalAmount():
    cursor = None
    try:
        batchid = int(input("\nEnter Batch ID: "))
        
        cursor = database.connect.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM batch WHERE id = %s AND is_deleted = 0", (batchid,))
        batch = cursor.fetchone()
        
        if not batch:
            print("\n[-] Active Batch ID not found.\n")
            return
            
        batch_title = batch.get('name') or batch.get('title') or f"Batch {batchid}"
            
        sql = """
            SELECT l.id, s.title AS subject_title, t.name AS teacher_name, 
                   l.duration_in_minutes, l.amount, l.lecturedate
            FROM lecture l
            INNER JOIN subject s ON l.subjectid = s.id
            INNER JOIN teacher t ON l.teacherid = t.id
            WHERE l.batchid = %s
            ORDER BY l.lecturedate ASC
        """
        cursor.execute(sql, (batchid,))
        lectures = cursor.fetchall()
        
        if not lectures:
            print(f"\n[-] No lecture records found for Batch '{batch_title}'.\n")
            return

        print(f"\n===================================================================================")
        print(f" BATCH LECTURE & FINANCIAL REPORT: {batch_title}")
        print(f"===================================================================================")
        print(f"{'ID':<5} {'Subject Title':<22} {'Teacher Name':<20} {'Min':<8} {'Amount':<10} {'Date':<12}")
        print("-" * 83)
        
        total_amount = 0.0
        total_duration = 0
        
        for row in lectures:
            print(f"{row['id']:<5} {row['subject_title']:<22} {row['teacher_name']:<20} {row['duration_in_minutes']:<8} {row['amount']:<10.2f} {str(row['lecturedate']):<12}")
            total_amount += float(row['amount'])
            total_duration += row['duration_in_minutes']
            
        print("-" * 83)
        print(f"{'TOTALS:':<48} {total_duration:<8} INR {total_amount:<10.2f}")
        print(f"===================================================================================\n")

    except Exception as e:
        print(f"\n[-] Error generating report: {e}\n")
    finally:
        if cursor:
            cursor.close()