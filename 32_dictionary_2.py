#dictionary
book = {} #empty dictionary
print(book)

#add key value pair
book['name'] = "Learning Data Science & ML"
book['chapter'] = [1,2,3,4,5] #chapter is list
book['topic'] = ('Introduction to ML & DS','python','library','algorithm','models') #tuple in list
book['price'] = 1000
print(book)


book['topic'][0] = 'index' #error as topics is tuple
book['chapter'][0] = 10 #change is possible chapter in list
del book['price'] #scalor value