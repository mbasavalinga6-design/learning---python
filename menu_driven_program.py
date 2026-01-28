def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


while True:
    print("\n--- SIMPLE CALCULATOR ---")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. EXIT")

    choice = int(input("Enter your choice: "))

    if choice in {1, 2, 3, 4}:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", mul(a, b))
    elif choice == 4:
        print("Result:", divide(a, b))
    elif choice == 5:
        print("--- EXITING PROGRAM ---")
        break
    else:
        print("You entered an invalid choice")
