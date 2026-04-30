class MyMath:
    #constructor
    def __init__(self,n1,n2):
        #create instance variable
        self.num1 = n1
        self.num2 = n2 
        print("constructor method is called.")
    def add(self):
        #here result is local variable (variable declared inside function without self is called local variable)
        result = self.num1 + self.num2
        print(f"addition = {result}") 

    def sub(self):
        result = self.num1 - self.num2 
        print(f"subtraction = {result}") 

    def mul(self):
        result = self.num1 * self.num2
        print(f'multiplication = {result}')

    def div(self):
        result = self.num1 / self.num2
        print(f'division = {result}')      

    #develop mul and div function like above 

#create object of MyMath class 
#object = className
a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
m1 = MyMath(a,b) # __init__ method is called automatically
m1.add()
m1.sub()
m1.mul()
m1.div()

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))

m2 = MyMath(n1=a,n2=b) # __init__ method is called automatically
m2.add()
m2.sub()
m2.mul()
m2.div()