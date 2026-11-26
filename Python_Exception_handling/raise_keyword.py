try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You are under age, you must be 18+")

except ValueError as e:
    print(e)

else:
    print("Access Granted!!")

finally:
    print("Program executed!! ")