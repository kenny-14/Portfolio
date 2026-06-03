amount = 0.0
menu = """
1. Check Balance
2. Withdraw Cash
3. Deposit Cash
4. Transfer Cash
0. Exit
"""
while True:
    print (menu)
    option = int(input('Select Option from Menu: '))
    if option == 0:
        print("Terminating Program......")
        break
    elif option == 1:
        print(f"Your current balance is: {amount}")
    elif option == 2:
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= amount:
            print(f"Initial Balance was: {amount}")
            amount -= withdraw
            print(f"Final Balance after withdrawing {withdraw} is: {amount}")
            print("Transaction completed successfully.")
        else:
            print("Insufficient Balance")
    elif option == 3:
        cash = float(input('deposit amount: '))
        print(f"Initial Balance was: {amount}")
        amount += cash
        print(f"Final Balance after depositing {cash} is: {amount}")
    elif option == 4:
        recipient = input("Enter recipient name: ")
        transfer = float(input("Enter amount to transfer: "))
        if transfer <= amount:
            print(f"Initial Balance was: {amount}")
            amount -= transfer
            print(f"Transfer of {transfer} to {recipient} successful.")
            print(f"Final Balance is: {amount}")
        else:
            print("Insufficient Balance")
        
    else:
        print("Option not available")
    print("Have a nice day!")
    