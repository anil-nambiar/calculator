#x = int(input("Enter first integer: "))
#y = int(input("Enter second integer: "))
x = 5
y = 5
n = 4
while True:
    print("Enter action:\n1. Add\n2. Subtract\n3. Multiply\n4. Exit\n")
    if n==1:
        print("Sum is", x+y)
    elif n==2:
        print("Difference is", x-y)
    elif n==3:
        print("Product is", x*y)
    elif n==4:
        print("File changed to test build! Goodbye!")
        break
