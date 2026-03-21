#operators
#write a program to display 3 digit amount into word.#567

amount = int(input("enter 3 digit amount"))
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six','seven', 'eight','nine']
print(amount)

last = amount % 10 # 7
print(last)

remaining = amount // 10 #56
print(remaining)

middle = remaining % 10 #6
print(middle)

first = remaining // 10 # 5
print(first)

print(first,middle,last)

print(words[first],words[middle],words[last])


      
