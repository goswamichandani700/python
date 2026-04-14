#write a program to filter all the players who have score more then 50 but less then 100 runs in match. use list and filter function
scores = [
    ("Virat", 72),
    ("Rohit", 45),
    ("Gill", 101),
    ("Hardik", 30),
    ("KL Rahul", 55),
    ("Surya", 99)
]
print(scores)
high_score = filter(lambda scores: scores[1]>50 and scores[1]<100,scores)
print(list(high_score))