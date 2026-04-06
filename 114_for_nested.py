'''
1 0 1 0 1
1 0 1 0
1 0 1
1		
'''
#only 1 astrik per print function 
#print("*")

for row in range(6,1,-1): #1 2 3 4 5 
    for column in range(1,row): #1 
        reminder = column % 2
        print(reminder,end=' ')
    #empty line
    print(' ')
    