#write a program that return volume of given length, width, depth 
def getvolume(length,width,depth):
    volume = length * width * depth
    return volume


length = int(input('enter length'))
width = int(input('enter width'))
depth = int(input('enter depth'))
answer = getvolume(length,width,depth)
print("volume=",answer)
