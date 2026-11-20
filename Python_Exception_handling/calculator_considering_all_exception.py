try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    op = input("Enter operator (+, -, *, /): ")

    # Perform calculation
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Invalid operator!")
except ValueError:
    print("Enter valiid numbers!!")
except ZeroDivisionError:
    print("Can not devide by zero!!")
finally:
    print("Execution Finished!!")