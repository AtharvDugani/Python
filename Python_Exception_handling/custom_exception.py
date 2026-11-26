class InvalidAgeException(Exception):
    pass
try:
    age = 15
    if age < 18:
        raise InvalidAgeException("You are Underage!!")
    print("good to go")
except InvalidAgeException as e:
    print(e)
else:
    print("Acess Granted!!")
finally:
    print("Program executed!!")