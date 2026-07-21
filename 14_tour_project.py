import tour as t 
import transaction as tr
import expense_reports as r 
while True:    
    print("\nPress 1 for tour management")
    print("Press 2 for transaction management")
    print("Press 3 for Report management")
    print("Press 0 for Exit")
    
    choice = int(input("enter your choice: "))

    if choice < 0 or choice > 3:
        print("invalid choice")
    else:
        if choice == 1:
            while True:
                # insert, update, Delete(update operation), View
                print("\nPress 1 to insert new tour")
                print("Press 2 to update tour")
                print("Press 3 to delete tour")
                print("Press 4 to view tour")
                print("Press 0 to exit to main menu")
                
                tour = int(input("enter your choice: "))
                
                if tour < 0 or tour > 4:
                    print("invalid choice")
                else:
                    if tour == 1:
                        t.AddTour()
                    elif tour == 2:
                        t.ViewTour()
                        t.UpdateTour()
                    elif tour == 3:
                        t.ViewTour()
                        t.DeleteTour()
                    elif tour == 4:
                        t.ViewTour()
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        elif choice == 2:    
            while True:
                # insert transaction, Delete transaction, Search transaction, View transaction
                print("\nPress 1 to insert tour_name to transaction")
                print("Press 2 to delete tour_name from transaction")
                print("Press 3 to search tour_name in transaction")
                print("Press 4 to view all transaction ")
                print("Press 0 to exit to main menu")
                
                transaction_choice = int(input("enter your choice: "))
                
                if transaction_choice < 0 or transaction_choice > 4:
                    print("invalid choice")
                else:
                    if transaction_choice == 1:
                        tr.AddTransaction()
                    elif transaction_choice == 2:
                        tr.DeleteTransaction()
                    elif transaction_choice == 3:
                        tr.SearchTransaction()
                    elif transaction_choice == 4:
                        tr.DisplayTransaction()
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        elif choice == 3:
            while True:
                # monthly, quarter,year,tour wise income expense report(tour id will given by user),tour wise income expense report(all tour)
                print("\nPress 1 to generate month wise expense report")
                print("Press 2 for Quarter Wise Income Expense Report")
                print("Press 3 for Year Wise Income Expense Report")
                print("Press 4 for Tour Wise Income Expense Report")
                print("Press 5 for All Tour Income Expense Report")
                print("Press 0 to Exit to Main Menu")

                report_choice = int(input("Enter your choice : "))

                if report_choice < 0 or report_choice > 5:
                    print("Invalid Choice")

                else:
                    if report_choice == 1:
                        r.MonthWiseIncomeExpenseReport()

                    elif report_choice == 2:
                        r.QuarterWiseIncomeExpenseReport()

                    elif report_choice == 3:
                        r.YearWiseIncomeExpenseReport()

                    elif report_choice == 4:
                        r.TourWiseIncomeExpenseReport()

                    elif report_choice == 5:
                        r.AllTourIncomeExpenseReport()

                    else:
                        print("Exit to Main Menu")
                break