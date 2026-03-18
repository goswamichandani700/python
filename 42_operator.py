#write a program to convert no of balls into hours and remaining ball in cricket.

balls = int(input('enter ball'))

hours = balls // 60
hours = hours % 60

print('balls=',balls, 'hours=',hours) 