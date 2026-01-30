def menu():
    print("\n-- BANKING SYSTEM --")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

balance = 0

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your current balance is:", balance)

    elif choice == 2:
        deposit = float(input("Enter the money to deposit: "))
        balance += deposit
        print("Money deposited successfully")

    elif choice == 3:
        money = float(input("Enter the money to withdraw: "))
        if money <= balance:
            balance -= money
            print("Withdrawn money:", money)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using our banking system")
        break

    else:
        print("You entered an invalid number")
