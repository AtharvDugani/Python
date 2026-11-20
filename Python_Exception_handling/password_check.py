try:
    password = input("Enter a password: ")
    if not password.isalpha():
        raise ValueError("Enter Characters only!!")
    
except ValueError as e:
    print(e)
else:
    print("Logged in successfuly!!")
finally:
    print("Authentication Complete")