try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age 
    print(f"Your age is {age}")
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

# we use try and except block to handle exceptions that are 
# raised in our programs. As a good programmer, we should always
# anticipate this kind of issues and handle them properly.