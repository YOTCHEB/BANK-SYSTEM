# Dictionary to store account information
Bank_store = {}
# Dictionary to store transaction history
Transaction_history = {}

# Function to create a new account
def create_account():
    account_number = input("Enter your account number: ")
    account_name = input("Enter your account name: ")
    account_balance = input("Enter your account balance: ")
    account_type = input("Enter account type (savings/current): ")
    account_password = input("Enter your account password: ")
    # Store account details in the Bank_store dictionary
    Bank_store[account_number] = [account_name, account_balance, account_type, account_password]
    # Initialize an empty transaction history for the account
    Transaction_history[account_number] = []
    print(f"Account created with {account_name} and account number: {account_number} successfully")

# Function to verify the account password
def verify_password(account_number):
    password = input("Enter your account password: ")
    if Bank_store[account_number][3] == password:
        return True
    else:
        print("Incorrect password")
        return False

# Function to deposit money into an account
def deposit():
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        amount = input("Enter the amount to deposit: ")
        # Update the account balance
        Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) + int(amount))
        # Record the transaction
        Transaction_history[account_number].append(f"Deposited {amount}")
        print(f"Deposit of {amount} to account {account_number} successful")

# Function to withdraw money from an account
def withdraw():
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        amount = input("Enter the amount to withdraw: ")
        # Update the account balance
        Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) - int(amount))
        # Record the transaction
        Transaction_history[account_number].append(f"Withdrew {amount}")
        print(f"Withdrawal of {amount} from account {account_number} successful")

# Function to send money to another account
def send_money():
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

# Function to make a payment to a biller
def make_payment():
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
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

# Function to check the account balance
def check_balance():
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        print(f"Your balance is {Bank_store[account_number][1]}")

# Function to calculate interest for savings accounts
def calculate_interest():
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        if Bank_store[account_number][2] == "savings":
            interest = int(Bank_store[account_number][1]) * 0.04
            # Update the account balance with the interest
            Bank_store[account_number][1] = str(int(Bank_store[account_number][1]) + interest)
            print(f"Interest added: {interest}")
        else:
            print("Interest calculation is only for savings accounts")

# Function to view the transaction history
def view_transaction_history():
    account_number = input("Enter your account number: ")
    if verify_password(account_number):
        print("Transaction history:")
        for transaction in Transaction_history[account_number]:
            print(transaction)

# Function to display the account menu
def account_menu():
    while True:
        print("1. Create Account")
        print("2. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            break
        else:
            print("Invalid choice")

# Function to display the transaction menu
def transaction_menu():
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Send Money")
        print("4. Make Payment")
        print("5. Back to Main Menu")
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
        print("1. Check Balance")
        print("2. Calculate Interest")
        print("3. Back to Main Menu")
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
        print("1. View Transaction History")
        print("2. Back to Main Menu")
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
        print("1. Create Account")
        print("2. Exit")
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
            print("1. Account Menu")
            print("2. Transaction Menu")
            print("3. Balance Menu")
            print("4. History Menu")
            print("5. Exit")
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
