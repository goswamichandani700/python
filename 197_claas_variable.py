class Society:
    #class variable
    hall = "ABC Community Hall"
    def __init__(self,flatno,owner):
        self.flatno = flatno 
        self.owner = owner
    def display(self):
        print("Flat No ",self.flatno)
        print("Owner = ",self.owner)
    

print("Hall ",Society.hall) # ABC Community Hall
Society.hall = 'XYZ Marriage Hall'
print("Hall ",Society.hall) # ABC Community Hall

s1 = Society(101,'Chandani Goswami')
s2 = Society(102,'Bhumika Goswami')
s3 = Society(103,'Vishal Goswami')
s4 = Society(103,'shriddhi Goswami')
s5 = Society(105,'Ashwingiri Goswami')

s1.display()
s2.display()
s3.display()
s4.display()
s5.display()

print("Hall ",s1.hall)
print("Hall ",s2.hall)
print("Hall ",s3.hall)
print("Hall ",s4.hall)
print("Hall",s5.hall)