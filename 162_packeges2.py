#Create Package India which has 4 sub package 
import india.north.language as no 
import india.south.language as so 
import india.east.language as ea
import india.west.language as we

print(no.getlanguage())
print(so.getlanguage())
print(ea.getlanguage())
print(we.getlanguage())

result = no.islanguageexist("Gujrati")
print(f"is gujrati existing in north_india ",result)

result = so.islanguageexist("Hindi")
print(f"is hindi existing in south_india ",result)

result = ea.islanguageexist("Bengali")
print(f"is gujrati existing in east_india ",result)

result = we.islanguageexist("Bihari")
print(f"is bihari existing in west_india ",result)







