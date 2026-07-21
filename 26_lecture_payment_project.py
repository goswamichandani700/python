import course as c
import batch as b  # Imported batch management module
import subject as s
import teacher as t
import lecture as l

while True:    
    print("\n--- Main Menu ---")
    print("Press 1 for Course Management")
    print("Press 2 for Batch Management")
    print("Press 3 for Subject Management")
    print("Press 4 for Teacher Management")
    print("Press 5 for Lecture Management")
    print("Press 6 for Payout Management")
    print("Press 7 for Reports")
    print("Press 0 for Exit")
    
    choice = int(input("Enter your choice: "))

    if choice < 0 or choice > 7:
        print("Invalid choice")
    else:
        # 1. Course Management
        if choice == 1:
            while True:
                print("\n--- Course Management ---")
                print("Press 1 to insert course")
                print("Press 2 to update course")
                print("Press 3 to delete course")
                print("Press 4 to select course")
                print("Press 5 to search course")
                print("Press 0 to exit to main menu")
                
                course_choice = int(input("Enter your choice: "))
                
                if course_choice < 0 or course_choice > 5:
                    print("invalid choice")
                elif course_choice == 1:
                    c.InsertCourse()
                elif course_choice == 2:
                    c.SelectCourse()
                    c.UpdateCourse()
                elif course_choice == 3:
                    c.SelectCourse()
                    c.DeleteCourse()
                elif course_choice == 4:
                    c.SelectCourse()
                elif course_choice == 5:
                    c.SearchCourse()
                else:
                    print("Exiting to main menu...")
                    break
        
        # 2. Batch Management
        elif choice == 2:    
            while True:
                print("\n--- Batch Management ---")
                print("Press 1 to insert batch")
                print("Press 2 to update batch")
                print("Press 3 to delete batch")
                print("Press 4 to select batch")
                print("Press 5 to search batch")
                print("Press 0 to exit to main menu")
                
                batch_choice = int(input("Enter your choice: "))
                
                if batch_choice < 0 or batch_choice > 5:
                    print("Invalid choice")
                elif batch_choice == 1:
                    b.InsertBatch()
                elif batch_choice == 2:
                    b.SelectBatch()
                    b.UpdateBatch()
                elif batch_choice == 3:
                    b.SelectBatch()
                    b.DeleteBatch()
                elif batch_choice == 4:
                    b.SelectBatch()
                elif batch_choice == 5:
                    b.SearchBatch()
                else:
                    print("Exiting to main menu...")
                    break
        
        # 3. Subject Management
        elif choice == 3:
            while True:
                print("\n--- Subject Management ---")
                print("Press 1 to insert subject")
                print("Press 2 to update subject")
                print("Press 3 to delete subject")
                print("Press 4 to select subject")
                print("Press 5 to search subject")
                print("Press 0 to exit to main menu")
                
                subject_choice = int(input("Enter your choice: "))
                
                if subject_choice < 0 or subject_choice > 5:
                    print("Invalid choice")
                elif subject_choice == 1:
                    s.InsertSubject()
                elif subject_choice == 2:
                    s.SelectSubject()
                    s.UpdateSubject()
                elif subject_choice == 3:
                    s.SelectSubject()
                    s.DeleteSubject()
                elif subject_choice == 4:
                    s.SelectSubject()
                elif subject_choice == 5:
                    s.SearchSubject()
                else:
                    print("Exiting to main menu...")
                    break

        # 4. Teacher Management
        elif choice == 4:
            while True:
                print("\n--- Teacher Management ---")
                print("Press 1 to insert teacher")
                print("Press 2 to update teacher")
                print("Press 3 to delete teacher")
                print("Press 4 to select teacher")
                print("Press 5 to search teacher")
                print("Press 0 to exit to main menu")
                
                teacher_choice = int(input("Enter your choice: "))
                
                if teacher_choice < 0 or teacher_choice > 5:
                    print("Invalid choice")
                elif teacher_choice == 1:
                    t.InsertTeacher()
                elif teacher_choice == 2:
                    t.SelectTeacher()
                    t.UpdateTeacher()
                elif teacher_choice == 3:
                    t.SelectTeacher()
                    t.DeleteTeacher()
                elif teacher_choice == 4:
                    t.SelectTeacher()
                elif teacher_choice == 5:
                    t.SearchTeacher()
                else:
                    print("Exiting to main menu...")
                    break

        # 5. Lecture Management
        elif choice == 5:
            while True:
                print("\n--- Lecture Management ---")
                print("Press 1 to insert lecture")
                print("Press 2 to select lecture")
                print("Press 0 to exit to main menu")
                
                lecture_choice = int(input("Enter your choice: "))
                
                if lecture_choice < 0 or lecture_choice > 2:
                    print("Invalid choice")
                elif lecture_choice == 1:
                    l.InsertLecture()
                elif lecture_choice == 2:
                    l.SelectLecture()
                else:
                    print("Exiting to main menu...")
                    break

        # 6. Payout Management
        elif choice == 6:
            while True:
                print("\n--- Payout Management ---")
                print("Press 1 to generate payout of specific teacher between given dates")
                print("Press 2 to generate PDF of payment and email admin and teacher")
                print("Press 0 to exit to main menu")
                
                payout_choice = int(input("Enter your choice: "))
                
                if payout_choice < 0 or payout_choice > 2:
                    print("Invalid choice")
                elif payout_choice == 1:
                    print("Generating specific teacher payout by date...")
                elif payout_choice == 2:
                    print("Generating PDF and sending emails to admin and teacher...")
                else:
                    print("Exiting to main menu...")
                    break

        # 7. Reports
        elif choice == 7:
            while True:
                print("\n--- Reports Management ---")
                print("Press 1 to generate batch wise lecture detail between given dates")
                print("Press 2 to generate batch wise lecture detail with total amount")
                print("Press 0 to exit to main menu")
                
                report_choice = int(input("Enter your choice: "))
                
                if report_choice < 0 or report_choice > 2:
                    print("Invalid choice")
                elif report_choice == 1:
                    print("Generating batch wise lecture detail between given dates...")
                elif report_choice == 2:
                    print("Generating batch wise lecture detail with total amount...")
                else:
                    print("Exiting to main menu...")
                    break

        # 0. Exit
        else:
            print("Exiting from program...")
            break