#  write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
#     Aries: March 21–April 19
#     Taurus: April 20–May 20
#     Gemini: May 21–June 21
#     Cancer: June 22–July 22
#     Leo: July 23–August 22
#     Virgo: August 23–September 22
#     Libra: September 23–October 22
#     Scorpio: October 24–November 21
#     Sagittarius: November 22–December 21
#     Capricorn: December 22–January 19
#     Aquarius: January 20–February 18
#     Pisces: February 19–March 20

date = int(input("enter date"))
month = int(input("enter month"))
if (date>=21 and month==3) or (date<=19 and month==4):
    print("you are aries")
elif (date>=20 and month==4) or (date<=20 and month==5): 
    print("you are taurus")
elif (date>=21 and month==5) or (date<=21 and month==6):
    print("you are gemini ")
elif (date>=22 and month==6) or (date<=22 and month==7):
    print("you are cancer")
elif (date>=23 and month==7) or (date<=22 and month==8):
    print('you are leo')
elif (date>=23 and month==8) or (date<=22 and month==9):
    print("you are virgo")
elif (date>=23 and month==9) or (date<=22 and month==10):
    print("you are libra ")
elif (date>=24 and month==10) or (date<=21 and month==11):
    print("you are scorpio")
elif (date>=22 and month==11) or (date<=21 and month==12):
    print('you are sagittarius')
elif (date>=22 and month==12) or (date<=19 and month==1):
    print("you are capricorn")
elif (date>=20 and month==1) or (date<=18 and month==2):
    print("you are aquarius")
elif (date>=19 and month==2) or (date<=20 and month==3):
    print("you are pisces")                                 

