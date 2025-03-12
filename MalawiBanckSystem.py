
# Dictionary to store account information
Bank_store = {}
# Dictionary to store transaction history
Transaction_history = {}
# Dictionary to store daily withdrawal amounts
Daily_withdrawals = {}
# Dictionary to store incorrect password attempts
Incorrect_attempts = {}

# Function to create a new account
def create_account():
    print("----------------------------------------")
    while True:
        account_number = input("Enter your 13-digit account number: ")
        if len(account_number) == 13 and account_number.isdigit():
            break
        else:
            print("Invalid account number. It must be 13 digits.")
    
    account_name = input("Enter your account name: ")
    account_balance = input("Enter your account balance: ")
    account_type = input("Enter account type (savings/current): ")
    
    while True:
        account_password = input("Enter your account password (4 or 8 characters): ")
        if len(account_password) in [4, 8]:
            break
        else:
            print("Invalid password. It must be 4 or 8 characters.")
    
    while True:
        phone_number = input("Enter your 10-digit phone number: ")
        if len(phone_number) == 10 and phone_number.isdigit():
            break
        else:
            print("Invalid phone number. It must be 10 digits.")
    
    location = input("Enter your location: ")
    birthday = input("Enter your birthday (YYYY-MM-DD): ")
    gender = input("Enter your gender (M/F): ")
    
    # Store account details in the Bank_store dictionary
    Bank_store[account_number] = [account_name, account_balance, account_type, account_password, phone_number, location, birthday, gender]
    # Initialize an empty transaction history for the account
    Transaction_history[account_number] = []
    # Initialize daily withdrawal amount to 0
    Daily_withdrawals[account_number] = 0
    # Initialize incorrect password attempts to 0
    Incorrect_attempts[account_number] = 0
    print(f"Account created successfully for {account_name} with account number: {account_number}")
    print("----------------------------------------------------------------------------------------")

# Function to verify the account password
def verify_password(account_number):
    if Incorrect_attempts[account_number] >= 3:
        print("Account is locked due to too many incorrect password attempts.")
        return False
    
    password = input("Enter your account password: ")
    if Bank_store[account_number][3] == password:
        Incorrect_attempts[account_number] = 0
        return True
    else:
        Incorrect_attempts[account_number] += 1
        print("Incorrect password")
        return False

# Function to change the account password
def change_password():
    print("-----------------------------------------------------------------------------------")
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        while True:
            new_password = input("Enter your new account password (4 or 8 characters): ")
            if len(new_password) in [4, 8]:
                Bank_store[account_number][3] = new_password
                print("Password changed successfully")
                break
            else:
                print("Invalid password. It must be 4 or 8 characters.")
    print("-----------------------------------------------------------------------------------")

# Function to deposit money into an account
def deposit():
    print("---------------------------------------------------------------------------------------")
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        amount = input("Enter the amount to deposit: ")
        # Update the account balance
        Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) + int(amount))
        # Record the transaction
        Transaction_history[account_number].append(f"Deposited {amount}")
        print(f"Deposit of {amount} to account {account_number} successful")
    print("-------------------------------------------------------------------------------------------")

# Function to withdraw money from an account with a daily limit
def withdraw():
    print("-------------------------------------------------------------------------------------")
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        amount = int(input("Enter the amount to withdraw: "))
        description = input("Enter the description for the withdrawal: ")
        daily_limit = 1000  # Set daily withdrawal limit
        if Daily_withdrawals[account_number] + amount > daily_limit:
            print("Daily withdrawal limit exceeded")
        elif int(Bank_store[account_number][1]) < amount:
            print("Insufficient balance")
        else:
            # Update the account balance
            Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) - amount)
            # Update the daily withdrawal amount
            Daily_withdrawals[account_number] += amount
            # Record the transaction
            Transaction_history[account_number].append(f"Withdrew {amount} - {description}")
            print(f"Withdrawal of {amount} from account {account_number} successful")
    print("-------------------------------------------------------------------------------------")

# Function to send money to another account
def send_money():
    print("------------------------------------------------------------------------------------")
    sender_account = input("Enter your account number: ")
    if verify_password(sender_account):
        receiver_account = input("Enter the receiver's account number: ")
        if receiver_account in Bank_store:
            amount = input("Enter the amount to send: ")
            if int(Bank_store[sender_account][1]) >= int(amount):
                # Update the sender's and receiver's account balances
                Bank_store[sender_account][1] = str(int(Bank_store[sender_account][1]) - int(amount))
                Bank_store[receiver_account][1] = str(int(Bank_store[receiver_account][1]) + int(amount))
                # Record the transaction
                Transaction_history[sender_account].append(f"Sent {amount} to {receiver_account}")
                Transaction_history[receiver_account].append(f"Received {amount} from {sender_account}")
                print(f"Sent {amount} to {receiver_account} successfully")
            else:
                print("Insufficient balance")
        else:
            print("Receiver's account number not found")
    print("--------------------------------------------------------------------------------------")

# Function to make a payment to a biller, employer, or for buying items
def make_payment():
    print("-----------------------------------------------------------------------------------------")
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        print("1. Pay Biller")
        print("2. Pay Employer")
        print("3. Buy Items")
        payment_choice = input("Enter your choice: ")
        if payment_choice == "1":
            biller = input("Enter the biller name: ")
            amount = input("Enter the amount to pay: ")
            if int(Bank_store[account_number][1]) >= int(amount):
                # Update the account balance
                Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) - int(amount))
                # Record the transaction
                Transaction_history[account_number].append(f"Paid {amount} to {biller}")
                print(f"Paid {amount} to {biller} successfully")
            else:
                print("Insufficient balance")
        elif payment_choice == "2":
            employer = input("Enter the employer name: ")
            amount = input("Enter the amount to pay: ")
            if int(Bank_store[account_number][1]) >= int(amount):
                # Update the account balance
                Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) - int(amount))
                # Record the transaction
                Transaction_history[account_number].append(f"Paid {amount} to {employer}")
                print(f"Paid {amount} to {employer} successfully")
            else:
                print("Insufficient balance")
        elif payment_choice == "3":
            item = input("Enter the item name: ")
            amount = input("Enter the amount to pay: ")
            if int(Bank_store[account_number][1]) >= int(amount):
                # Update the account balance
                Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) - int(amount))
                # Record the transaction
                Transaction_history[account_number].append(f"Bought {item} for {amount}")
                print(f"Bought {item} for {amount} successfully")
            else:
                print("Insufficient balance")
        else:
            print("Invalid choice")
    print("----------------------------------------------------------------------------------")

# Function to check the account balance
def check_balance():
    print("-----------------------------------------------------------------------------------")
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        print(f"Your balance is {Bank_store[account_number][1]}")
    print("----------------------------------------------------------------------------------")

# Function to calculate interest for savings accounts
def calculate_interest():
    print("-----------------------------------------------------------------------------")
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        if Bank_store[account_number][2] == "savings":
            interest = int(Bank_store[account_number][1]) * 0.04
            # Update the account balance with the interest
            Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) + interest)
            print(f"Interest added: {interest}")
        else:
            print("Interest calculation is only for savings accounts")
    print("-------------------------------------------------------------------------------")

# Function to view the transaction history
def view_transaction_history():
    print("----------------------------------------------------------------------------------")
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        print("Transaction history:")
        for transaction in Transaction_history[account_number]:
            print(transaction)
    print("--------------------------------------------------------------------------------------")

# Function to display the account menu
def account_menu():
    while True:
        print("Account Menu")
        print("-----------------------------------")
        print("1. Create Account")
        print("2. Change Password")
        print("3. Back to Main Menu")
        print("-----------")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            change_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

# Function to display the transaction menu
def transaction_menu():
    while True:
        print("Transaction Menu")
        print("---------------------------------------------------------------------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Send Money")
        print("4. Make Payment")
        print("5. Back to Main Menu")
        print("-----------------------------------------------------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            send_money()
        elif choice == "4":
            make_payment()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

# Function to display the balance menu
def balance_menu():
    while True:
        print("Balance Menu")
        print("----------------------------------------------------------------")
        print("1. Check Balance")
        print("2. Calculate Interest")
        print("3. Back to Main Menu")
        print("-----------------------------------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            calculate_interest()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

# Function to display the history menu
def history_menu():
    while True:
        print("History Menu")
        print("---------------------------------------------------------------")
        print("1. View Transaction History")
        print("2. Back to Main Menu")
        print("-----------")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_transaction_history()
        elif choice == "2":
            break
        else:
            print("Invalid choice")

# Main function to start the program
def main():
    while True:
        print("Welcome to National Bank of Malawi")
        print("---------------------------------------------------------------------")
        print("1. Create Account")
        print("2. Exit")
        print("---------------------------------------------------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
            break
        elif choice == "2":
            return
        else:
            print("Invalid choice")

    account_number = input("Enter your account number to log in: ")
    if verify_password(account_number):
        print(f"Welcome, {Bank_store[account_number][0]}!")
        while True:  
            print("Main Menu")
            print("-------------------------------------------------------------------------")
            print("1. Account Menu")
            print("2. Transaction Menu")
            print("3. Balance Menu")
            print("4. History Menu")
            print("5. Exit")
            print("---------------------------------------------------------------------")
            choice = input("Enter your choice: ")
            if choice == "1":
                account_menu()
            elif choice == "2":
                transaction_menu()
            elif choice == "3":
                balance_menu()
            elif choice == "4":
                history_menu()
            elif choice == "5":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    main()
