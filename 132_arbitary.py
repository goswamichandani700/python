#write a program to display on that cities whose name end with nagar from all the cities passed as argument
def nagar_cities(*cities):
    for city in cities:
        if "nagar" in city:
            print(city)

# Example
nagar_cities("Ahmedabad", "Jamnagar", "Bhavnagar", "Surat", "Gandhinagar")