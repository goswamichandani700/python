#write a program to convert inches into foot and remaining inches.

inches = int(input('enter inches '))

foot = inches // 12
foot = inches % 12

print('foot=',foot, 'inches=',inches)
