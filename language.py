east_india = [
    "Assamese",
    "Bengali",
    "Bodo",
    "Maithili",
    "Manipuri",
    "Odia",
    "Santali"
]

def getlanguage():
   global east_india
   return east_india
    
   

def islanguageexist(languagename):
   global east_india
   result = languagename in east_india
   return result
    