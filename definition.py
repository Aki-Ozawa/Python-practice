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