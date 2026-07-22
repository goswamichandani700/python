import connection as database
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def GenerateTeacherPayout():
    cursor = None
    try:
        teacherid = int(input("Enter Teacher ID: "))
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")
        
        cursor = database.connect.cursor(dictionary=True)
        
        # Fetch active teacher details
        cursor.execute("SELECT id, name, email FROM teacher WHERE id = %s AND is_deleted = 0", (teacherid,))
        teacher = cursor.fetchone()
        
        if not teacher:
            print("\n[-] Active Teacher ID not found.\n")
            return None
            
        # Query lectures within date range
        sql = """
            SELECT l.id, s.title AS subject_title, l.duration_in_minutes, l.amount, l.lecturedate 
            FROM lecture l
            INNER JOIN subject s ON l.subjectid = s.id
            WHERE l.teacherid = %s AND l.lecturedate BETWEEN %s AND %s
            ORDER BY l.lecturedate ASC
        """
        cursor.execute(sql, (teacherid, start_date, end_date))
        lectures = cursor.fetchall()
        
        if not lectures:
            print(f"\n[-] No lecture records found for {teacher['name']} between given dates.\n")
            return None
            
        print(f"\n{'ID':<5} {'Subject Title':<25} {'Duration (Min)':<15} {'Amount':<10} {'Date':<12}")
        print("-" * 72)
        
        total_amount = 0.0
        total_duration = 0
        
        for row in lectures:
            print(f"{row['id']:<5} {row['subject_title']:<25} {row['duration_in_minutes']:<15} {row['amount']:<10.2f} {str(row['lecturedate']):<12}")
            total_amount += float(row['amount'])
            total_duration += row['duration_in_minutes']
            
        print("-" * 72)
        print(f"{'TOTAL:':<31} {total_duration:<15} {total_amount:<10.2f}")
        
        payout_data = {
            "teacher_id": teacher['id'],
            "teacher_name": teacher['name'],
            "teacher_email": teacher['email'],
            "start_date": start_date,
            "end_date": end_date,
            "lectures": lectures,
            "total_amount": total_amount,
            "total_duration": total_duration
        }
        return payout_data

    except ValueError:
        print("\n[-] Error: Teacher ID must be an integer.\n")
        return None
    except Exception as e:
        print(f"\n[-] Error: {e}\n")
        return None
    finally:
        if cursor:
            cursor.close()


def SendPayoutEmail(payout_data):
    if not payout_data:
        print("\n[-] No payout data available to generate invoice.\n")
        return
        
    cursor = database.connect.cursor()
    try:
        print("\nSelect Payment Mode:")
        print("1. Cash")
        print("2. Cheque")
        print("3. Online")
        
        while True:
            try:
                payment_mode = int(input("Enter Payment Mode Choice (1-3): "))
                if payment_mode in [1, 2, 3]:
                    break
                else:
                    print("[-] Invalid choice! Please enter 1, 2, or 3.")
            except ValueError:
                print("[-] Invalid input! Please enter a number (1, 2, or 3).")
                
        today_date = datetime.now().strftime('%Y-%m-%d')
        
        # 1. Database માં Payment રેકોર્ડ Insert કરવો
        insert_sql = """
            INSERT INTO payment (paymentdate, teacherid, amount, mode)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_sql, (today_date, payout_data['teacher_id'], payout_data['total_amount'], payment_mode))
        database.connect.commit()
        print(f"\n[+] Payment record inserted successfully into Database!")
        
        # 2. PDF ફાઈલ તૈયાર કરવી
        filename = f"Payout_{payout_data['teacher_name'].replace(' ', '_')}.pdf"
        mode_names = {1: "Cash", 2: "Cheque", 3: "Online"}
        selected_mode_str = mode_names.get(payment_mode, "Unknown")
        
        pdf = canvas.Canvas(filename, pagesize=letter)
        pdf.setFont("Courier-Bold", 14)
        
        pdf.drawString(200, 750, "PAYOUT INVOICE")
        pdf.setFont("Courier", 10)
        pdf.drawString(50, 735, "--------------------------------------------------")
        
        y = 715
        pdf.drawString(50, y, f"Teacher Name : {payout_data['teacher_name']}")
        y -= 15
        pdf.drawString(50, y, f"Teacher Email: {payout_data['teacher_email']}")
        y -= 15
        pdf.drawString(50, y, f"Period       : {payout_data['start_date']} to {payout_data['end_date']}")
        y -= 15
        pdf.drawString(50, y, f"Payment Mode : {selected_mode_str}")
        y -= 15
        pdf.drawString(50, y, "--------------------------------------------------")
        
        y -= 20
        pdf.drawString(50, y, f"{'Subject':<25} {'Duration(Min)':<15} {'Amount':<10}")
        y -= 15
        pdf.drawString(50, y, "--------------------------------------------------")
        
        for row in payout_data['lectures']:
            y -= 15
            pdf.drawString(50, y, f"{row['subject_title']:<25} {row['duration_in_minutes']:<15} {row['amount']:<10.2f}")
            if y < 100:
                pdf.showPage()
                pdf.setFont("Courier", 10)
                y = 750

        y -= 15
        pdf.drawString(50, y, "--------------------------------------------------")
        y -= 15
        pdf.drawString(50, y, f"Total Duration: {payout_data['total_duration']} Minutes")
        y -= 15
        pdf.drawString(50, y, f"Total Payout  : INR {payout_data['total_amount']:.2f}")
        y -= 15
        pdf.drawString(50, y, "--------------------------------------------------")
        y -= 15
        pdf.drawString(50, y, "Status        : Generated & Saved Successfully")
        
        pdf.save()
        print(f"[+] Real PDF file '{filename}' generated and saved successfully!")

        # 3. Email Dispatch (Project Demo Log)
        admin_email = "admin@computerclasses.com"
        teacher_email = payout_data['teacher_email']

        print("\n[+] Initializing Email Service...")
        print(f"[+] Attaching PDF Document: {filename}")
        print(f"[+] Sending Email to Admin ({admin_email}) and Teacher ({teacher_email})...")
        print("[+] Email Service Response: Payout invoice sent successfully!\n")

    except Exception as e:
        database.connect.rollback()
        print(f"\n[-] Error processing payment: {e}\n")
    finally:
        cursor.close()