print("Calculator Initiated!!")
print("Here we Go!!")
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")

else:
    print("Prgram Executed Successfuly!!")

finally:
    print("Finally the calculation is done!!")