#write a program to convert amount into words 
    #input: 12345 print: one two three four five 
def printwords(numbers):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six','seven', 'eight','nine']

    if numbers > 0:
    
        reminder = numbers % 10
        remaining = numbers // 10
        printwords(numbers//10)
        print(words[reminder], end=' ')

numbers = int(input("Enter number"))
printwords(numbers)



      






