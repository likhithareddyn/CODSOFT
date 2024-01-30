#Simplecalculator
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("""Choose an operation from given list:
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      """)
operation = int(input("Enter your choice number: "))
#performing arthemetic operations
if operation == 1:
    print("Add: {} + {} = {}".format(a,b,a+b))
elif operation == 2:
    print("Subtract: {} - {} = {}".format(a,b,a-b))
elif operation == 3:
    print("Multiply: {} * {} = {}".format(a,b,a*b))
elif operation == 4:
    print("Divide: {} / {} = {}".format(a,b,a/b))
else:
    print("Invalid Input")
