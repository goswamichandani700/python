#create function that return total Seconds of given hours, minutes and seconds. in this example minutes and second should be optional 
def getseconds(hours,minutes=0,seconds=0):
    totalseconds = (hours * 3600) + (minutes * 60) + seconds
    return totalseconds

hours = int(input('enter hours'))
minutes = int(input('enter minutes'))
seconds = int(input('enter seconds'))

result = getseconds(hours,minutes,seconds)
print("result into seconds using 3 arguments",result)

result = getseconds(hours,minutes)
print("result into seconds using 2 arguments",result)

result = getseconds(hours)
print("result into seconds using 1 arguments",result)
