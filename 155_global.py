# create variable count with value 100 
# create function sendSMS()
#     which will access global variable count 
#     and it will reduce count variable by 1 
#     and display message SMS send 
    
#     call sendSMS() function and also display count variable value after function called.

count = 100
def sendsms(amount):
    global count
    count = count - amount

print(count)
sendsms(1)
print("after update count is",count)



