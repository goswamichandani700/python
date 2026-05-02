# create class tour to store below tour detail 
#         id,title,days,price,detail 
#         it also has one class variable which store tour operator name 
#         it should also have  constructor, display(display all instance variable ) method 
#         and display tour operator name outside class
class tour:
   operator = "shiv travels"
   def __init__(self,id,title,days,price,details):
      self.id = id
      self.title = title
      self.days = days
      self.price = price
      self.details = details
   def display(self):
      print("id",self.id)
      print("title",self.title)
      print("days",self.days)
      print("price",self.price)
      print("details",self.details)
      print('operator',tour.operator)

   # create object
t1 = tour(1, "Goa Tour", 3, 10000, "Beach + Hotel")

# display instance data
t1.display()   


print('operator (before)',tour.operator) 
tour.operator = "bhairava travels" 
print('operator (after)',  tour.operator) 






