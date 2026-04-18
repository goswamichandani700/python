south_india = [
    "Kannada",
    "Malayalam",
    "Tamil",
    "Telugu"
]
def getlanguage():
    global south_india
    return south_india
    
   

def islanguageexist(languagename):
    global south_india
    result = languagename in south_india
    return result
    