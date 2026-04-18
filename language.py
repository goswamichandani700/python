north_india = [
    "Dogri",
    "Hindi",
    "Kashmiri",
    "Punjabi",
    "Sanskrit",
    "Urdu"
]

def getlanguage():
   global north_india
   return north_india
    
   

def islanguageexist(languagename):
   global north_india
   result = languagename in north_india
   return result
    