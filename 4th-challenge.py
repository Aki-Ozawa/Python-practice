# customer = {
#     "name": "John Smith", 
#     "age": 30,
#     "is_verified": True
# }
# customer["birthdate"] = "Jan 1 1997"
# print(customer["birthdate"])  

phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten"
}

output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)

# when the character is not found in the dictiinary, it used "!"