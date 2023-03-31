#create a dictionary 
capital_city = {
    "Iran" : "Tehran",
    "England" : "London",
    "China" : " Beijing",
    "France" : "Paris",
    "Chile" : "Santiago"
}

print('Original List: ', capital_city)

del capital_city["China"]

capital_city["Japan"] = "Tokoyo"

capital_city["Chile"] = "Hendoostan"

print('Updated list :', capital_city)
