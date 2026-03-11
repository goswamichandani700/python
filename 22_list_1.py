fruits =[] #empty list
nuts = ['cashew', 'almond', 'walnut']
print(fruits)
fruits.append('mango')
fruits.append('pinapple')
fruits.append('watermelon')
#insert new items at begining
fruits.insert(0,'kiwi')
#insert new items at begining
fruits.insert(1,'graps')
print(fruits)
#merge nuts into fruits
fruits.extend(nuts)
print(fruits)
#remove items from 1st possition
fruits.pop(0)
print(fruits)


#make list empty(delete all items)
nuts.clear()
print(nuts)

