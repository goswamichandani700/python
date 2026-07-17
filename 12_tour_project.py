import tour as t    
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
                        print("let us add tour to transaction")
                    elif transaction_choice == 2:
                        print("let us delete tour from transaction")
                    elif transaction_choice == 3:
                        print("let us search tour in transaction")
                    elif transaction_choice == 4:
                        print("let us view tour in transaction")
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        elif choice == 3:
            while True:
                # monthly, quarter,year,tour wise income expense report(tour id will given by user),tour wise income expense report(all tour)
                print("\nPress 1 to generate monthly report")
                print("Press 2 to generate quarter report")
                print("Press 3 to generate year report")
                print("Press 4 to generate specific tour report (by Tour ID)")
                print("Press 5 to generate all tours report")
                print("Press 0 to exit to main menu")
                
                report_choice = int(input("enter your choice: "))
                
                if report_choice < 0 or report_choice > 5:
                    print("invalid choice")
                else:
                    if report_choice == 1:
                        print("let us generate monthly report")
                    elif report_choice == 2:
                        print("let us generate quarter report")
                    elif report_choice == 3:
                        print("let us generate year report")
                    elif report_choice == 4:
                        print("let us generate specific tour report")
                    elif report_choice == 5:
                        print("let us generate all tours report")
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        else:
            print("exit from program")
            break
    