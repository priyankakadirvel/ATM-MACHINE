import time

password = 1234  # Correct PIN
balance = 5000   # Initial balance

# Loop until the correct PIN is entered
while True:
    print("Please insert your Card : ")
    time.sleep(2)  # Simulate the time taken to insert the card
    pin = int(input("Enter your ATM pin : "))

    if pin == password:
        print("PIN accepted. Access granted.")
        break  # Exit the loop when the correct PIN is entered
    else:
        print("Wrong password, please try again.\n")

# Main ATM operations once the correct PIN is entered
while True:
    print("""
        1 == Check balance
        2 == Withdraw balance
        3 == Deposit balance
        4 == Exit
        """)
    
    try:
        option = int(input("Please enter your choice : "))
    except:
        print("Please enter a valid option : ")
        

    if option == 1:
        print(f"Your current balance is ₹{balance}")

    elif option == 2:
        withdraw_amount = int(input("Enter withdrawal amount : ₹"))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"₹{withdraw_amount} is debited from your account") 
            print(f"Your current balance is ₹{balance}")
        else:
            print("Insufficient balance.")

    elif option == 3:
        deposit_amount = int(input("Please enter deposit amount : ₹")) 
        balance += deposit_amount 
        print(f"₹{deposit_amount} is credited to your account") 
        print(f"Your updated balance is ₹{balance}") 

    elif option == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
