def greet_user ():
    print('Hi there!')
    print('Welcome abroad')

# inside a definition, they will not print since it is a definition

print("Start")
greet_user()
print("Finish")
 

def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome abroad')

print("Start")
greet_user("John")
print("Finish")

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name} !')
    print('Welcome abroad')

greet_user("Aki", "Ozawa")
greet_user(last_name="Ozawa", first_name="Kinako")

def square(number):
    return number * number

result = square(3)
print(result)  

# By default all functions in Python return none. So if you have a function that 
# calculates something, you can return the result using the return statement