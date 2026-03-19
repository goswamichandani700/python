countries = "india, china, japan, south korea, north korea, thailand, vietnam, indonesia, malaysia, singapore, philippines, nepal, bhutan, bangladesh, sri lanka, pakistan, afghanistan, iran, iraq, saudi arabia"


word = "india"
result = word in countries
print(result)

result = word not in countries
print(result)

word = "russia"
result = word in countries
print(result)

result = word not in countries
print(result)

fruits = ["apple", "banana", "mango", "orange", "grapes", "pineapple", "papaya", "guava", "watermelon", "cherry"]

item = "banana"

print(item in fruits)
print(item not in fruits)

places = ("varanasi", "haridwar", "rishikesh", "tirupati", "kedarnath", "badrinath", "amritsar", "bodh gaya", "shirdi", "vaishno devi")

location = "kedarnath"

print(location in places)
print(location not in places)
