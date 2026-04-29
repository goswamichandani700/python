from datetime import date

# custom exception
class InvalidDateError(Exception):
    pass

def acceptDate(msg):
    while True:   # loop until correct input
        try:
            print(msg)
            day = int(input("Enter day: "))
            month = int(input("Enter month: "))
            year = int(input("Enter year: "))
            
            birthday = date(year, month, day)
            return birthday
        
        except ValueError:
            print("Invalid date entered! Please try again.\n")

# main program
birthday_1 = acceptDate("Enter 1st brother's birth date")
birthday_2 = acceptDate("Enter 2nd brother's birth date")

if birthday_1 < birthday_2:
    print("1st brother is elder brother")
elif birthday_1 > birthday_2:
    print("2nd brother is elder brother")
else:
    print("Both brothers have same birth date")

print("Good bye")