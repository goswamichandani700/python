#write a program to filter all the players who have score more then 50 runs in match. use list and filter function 
scores = [
    ("Virat", 72),
    ("Rohit", 45),
    ("Gill", 88),
    ("Hardik", 30),
    ("KL Rahul", 55)
]
print(scores)

high_score = filter(lambda scores:  scores[1]>50 ,scores ) 
print(list(high_score))
