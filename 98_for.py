# write a program to count consonants in any case in given string  
name = input("enter string")
count = 0
consonants = [
    'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
    'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'
]
for letter in name:
    #print(letter)
    if letter in consonants:
        count = count + 1 
print(f"consonants = {count} ")        



