#create dictionary to store your college details like name, trust, principal, establishment year, address, city, courses etc
college  = {'name' : 'naimisharanya','trust' : None,'principal' : 'kahan sir','establishment year': 2014,'address' : 'sidsar road','city' : 'bhavnagar','courses': ['b.sc(chemistry)','b.sc(maths)','b.sc(microbiology)']}
print(college)

#update city
college['city'] = 'jamnagar'
 
#add state
college['state'] = 'Gujrat'
print(college)

#display keys
print(college.keys())

#display values
print(college.values())

#remove state
college.pop('state')

#remove last item
college.popitem()
print(college)

college2 = college.copy()
print(college2)
college.clear()
print(college2)


