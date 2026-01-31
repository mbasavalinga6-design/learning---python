def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

while True:
    print("\n--- FINAL MENU ---")
    print("1. Check Even or Odd")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("Enter a number: "))
        print("Result:", even_or_odd(n))

    elif choice == "2":
        print("Program ended")
        break

    else:
        print("Invalid choice")
