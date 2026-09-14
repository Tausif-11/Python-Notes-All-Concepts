
#              -----------------------
#
#                 Mini Banking System
#
#              ------------------------


print("---------------------------------------------------------")
print("---------------------------------------------------------")

print("\n Welcome to the Mini Bank of Mohammad Tausif")

print("---------------------------------------------------------")
print("---------------------------------------------------------")


# Account Creation

print("---------------------------------------------------------")
print(" \n CREATE YOUR ACCOUNT")
print("---------------------------------------------------------")

print("\n Please provide the following details to create your account:")

name = input("\n Enter your full name: ")

print(f"Account created for {name}!")

account_number = input("\n Create a unique account number (e.g., AC-XXXXXX): ")

pin = input("\n Create a 6-digit PIN for your account: ")


# Checking the accuracy and length of Account Number and PIN

if len(account_number) == 9 and account_number[0:3] == "AC-" and account_number[3:].isdigit():
    print(f"Your account number is: {account_number}")
else:
    print("Invalid account number!")
    print("Account number must follow this format: AC-XXXXXX")


if len(pin) != 6 or not pin.isdigit():
    print("\nInvalid PIN!")
    print("PIN must contain exactly 6 digits.")
else:
    print("\nAccount created successfully!")
    print("Account Holder:", name)
    print("Account Number:", account_number)

# Starting balance
balance = 0


print("\n===================================")
print("          ACCOUNT ACCESS MENU")
print("===================================")

entered_pin = input("\nPlease enter your 6-digit PIN to access your account: ")


# Verify PIN

if entered_pin != pin:

    print("\nIncorrect PIN!")
    print("Access denied.")

else:

    print("\nLogin successful!")
    print("Welcome,", name)

    print("\n================================")
    print("           BANK MENU")
    print("================================")

    print("A - Add Money")
    print("W - Withdraw Money")
    print("B - Check Balance")
    print("Q - Quit")

    choice = input("\nEnter your choice: ")


    # ==========================================
    # ADD MONEY
    # ==========================================

    if choice == "A" or choice == "a":

        amount = float(input("Enter amount to add: ₹"))

        if amount <= 0:

            print("\nInvalid amount!")
            print("Amount must be greater than ₹0.")

        else:

            balance = amount

            print(f"\n₹{amount} added to your account.")
            print(f"Current Balance: ₹{balance}")


    # ==========================================
    # WITHDRAW MONEY
    # ==========================================

    elif choice == "W" or choice == "w":

        if balance == 0:

            print("\nNo balance in account!")
            print("Please add money first.")

        else:

            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:

                print("\nInvalid amount!")

            elif amount > balance:

                print("\nInsufficient balance!")
                print("Your current balance is: ₹", balance)

            else:

                balance = balance - amount

                print("\nWithdrawal successful!")
                print("Amount Withdrawn: ₹", amount)
                print("Remaining Balance: ₹", balance)

                if balance == 0:

                    print("Warning: Your account has no balance!")

                elif balance < 1000:

                    print("Warning: Your balance is very low!")


    # ==========================================
    # CHECK BALANCE
    # ==========================================

    elif choice == "B" or choice == "b":

        if balance == 0:

            print("\nNo balance in account!")
            print("Please add money first.")

        else:

            print("\nYour current balance is: ₹", balance)

            if balance >= 50000:

                print("Account Status: High Balance")

            elif balance >= 10000:

                print("Account Status: Normal Balance")

            else:

                print("Account Status: Low Balance")


    # ==========================================
    # QUIT
    # ==========================================

    elif choice == "Q" or choice == "q":

        print("\n================================")
        print("       SESSION ENDED")
        print("================================")

        print("Thank you,", name)
        print("Your temporary banking session has ended.")

        # Data exists only while this program is running.
        # When the program ends, the variables disappear.


    # ==========================================
    # INVALID CHOICE
    # ==========================================

    else:

        print("\nInvalid choice!")
        print("Please select A, W, B or Q.")

     

      

