west_india = [
    "Gujarati",
    "Konkani",
    "Marathi",
    "Rajasthani"
]

def getlanguage():
   global west_india
   return west_india
    
   

def islanguageexist(languagename):
   global west_india
   result = languagename in west_india
   return result
    