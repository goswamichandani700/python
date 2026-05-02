# create class product to store below product Detail
#         id,name,price,weight 
#     it should have constructor, display(display all instance variable ) method and pricePerGram() method 
class product:
   store = 'Kmall'
   def __init__(self,id,name,price,weight): 
      self.id = id
      self.name = name
      self.price = price
      self.weight = weight
      print("constructor called....")
   def display(self):
      print("Id",self.id) 
      print('name',self.name)
      print('price',self.price)
      print('weight',self.weight)
      print('store',product.store)
   def price_per_gram(self):
      if self.weight != 0:
         return self.price / self.weight
      else:
         return 0
   
   
id = int(input('enter id'))
name = input('enter name')
price = int(input('enter price'))
weight = int(input('enter weight'))
             
             
m1 = product(id,name,price,weight)
m1.display()

ppg = m1.price_per_gram()
print(f"price per gram = {ppg}")
 




