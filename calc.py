x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

while True:
    n = int(input("Enter action:\n1. Add\n2. Subtract\n3. Exit\n"))
    if n==1:
        print("Sum is", x+y)
    elif n==2:
        print("Difference is", x-y)
    elif n==3:
        print("Goodbye!")
        break
