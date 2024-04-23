
# Import the BankAccount Class from the BankAccount module and create a list with 5 objects:
import BankAccount

from BankAccount import BankAccount

bank_accounts = [BankAccount("jsmith","1452",156.21), BankAccount("aobrien","9892",856.21), BankAccount("hpotter","6001",43.50), BankAccount("hgranger","6993")]



# Ask the user to enter a pin
pin = input("Please, enter your Pin: ")



# Find the BankAccount object in the list bank_accounts for which the pin matches
pin_validate = False
for data in bank_accounts:
    if data.pin == pin:
        user_object = data
        pin_validate = True

if pin_validate == False:
    print("The Pin was incorrect - This user doesn't exist.")
    exit()


# Create a while loop that repeatedly asks the users to enter one option:
while True:
    user_option = input("Select one option: 1 - Withdraw | 2 - Deposit| 3 - Check Balance | 4 - Check Overdraft Status | 5 - Exit: ")

    while user_option != "1" and user_option != "2" and user_option != "3" and user_option != "4" and user_option != "5":
        user_option = input("Select one option: 1 - Withdraw | 2 - Deposit| 3 - Check Balance | 4 - Check Overdraft Status | 5 - Exit: ")

    if user_option == "1":
        print("You want to Withdraw")
        try:
           amount = int(input("Please, type the value that you want to Withdraw:"))
           user_object.withdraw(amount)
           print("Transaction happened successfully")
        except:
           print("Something wrong happened")
           print("Transaction did not occur successfully")
    
    elif user_option == "2":
        print("You want to Deposit")
        try:
           amount = int(input("Please, type the value that you want to Deposit:"))
           user_object.deposit(amount)
           print("Transaction happened successfully")
        except:
           print("Something wrong happened")
           print("Transaction did not occur successfully")

    elif user_option == "3":
        print("You want to Check Balance")
        print(f"Your current balance is: {user_object.balance}")

    elif user_option == "4":
        print("You want to Check Overdraft Status")
        print(user_object.overdraft_status)

    elif user_option == "5":
        break

    else:
        print("Invalid option, try again.")

    

