from datetime import datetime
import random
import time


all_bank_accounts = {}
#Welcome Message
def welcome_message():   
    return "Welcome to Foxy Banking App!, how can we serve you today?"
welcome_message()

#Goodbye Message
def final_greeting():
    return "Thank you for your banking with us, Goodbye."
final_greeting()   

#Generate Account Number
def generate_acct_numb(acct_type):
    if acct_type == 'g':
         base_number = "1010"
    elif acct_type == 's':
         base_number = "2020"
    elif acct_type == 'c':
        base_number = "3030"
    
    acct_numb = ""
    for i in range(6):
        random_acct_num = random.randint(0,9)
        acct_numb += str(random_acct_num)
    final_acct_numb = base_number + acct_numb
    return final_acct_numb

generate_acct_numb()

#Bank's main menu for selection   
def main_menu():
    continue_main_menu = True
    
    while continue_main_menu:
        first_message = welcome_message()
        open_acct = input("To Open an Account, press '1': ")   
        existing_acct = input("For an Existing Account holder, press '2': ")
        debit_acct = input("To debit your account, press '3': ")
        credit_acct = input("To credit your account, press '4'")
        check_acct = input("To check your account, press 8")
        close_acct = input("To close your account, press '5': ")
        exit_menu = input("To exit the menu selection press 'x': ").title()
        
        if open_acct == 1:
            operate_open_acct = create_account()
        elif existing_acct == 2:
            ask_exisiting_acct = input("What will like to do today? To Debit your account press 'd' OR To Credit your account press 'c'").title()
            if ask_exisiting_acct == 'd':
                operate_existing_acct = debit_account()
            elif ask_exisiting_acct == 'c':
                operate_existing_acct = credit_account()
            elif ask_exisiting_acct == 'k':
                operate_existing_acct == check_account_info()
            elif ask_exisiting_acct != 'd' or ask_exisiting_acct != 'c' or ask_exisiting_acct != 'k':
                return_to_menu = input("Invalid entry, press 'f' to go back to the previous menu")
                if return_to_menu == 'f':
                    back_to_menu = main_menu()
        elif close_acct == '4':
            operate_close_account = close_account()        
        elif exit_menu == 'x':
            continue_main_menu = False
            last_message = final_greeting()
    
    
    return first_message, open_acct, existing_acct, debit_acct, credit_acct, close_acct, exit_menu, last_message, operate_open_acct, operate_existing_acct, operate_close_account, back_to_menu, check_acct
    
main_menu()

def create_account():
    open_acct = input("To Open an Account, press 1: ")
    if open_acct == "1":
        acct_type = input("What kind of account would you like to open? "\
            "press 'g' for 'Gold Account',"\
            "OR press 's' for 'Savings',"\
            "OR press 'c' for 'Chequing': ").strip().lower()
        
        print("\nProcessing account creation", end="")
        for _ in range(3):  
            time.sleep(0.5)  
            print(".", end="", flush=True)
        print("\n")  
        
        new_acct = {
            'Account Type': "Gold" if acct_type == 'g' else "Savings" if acct_type == 's' else "Chequing",
            'Account Number': generate_acct_numb(acct_type),
            'Account Bal': 0
        }
        
        print("Kindly provide the following details below: ")
        first_name = str(input("Enter your first name: "))
        new_acct['First Name'] = first_name
        last_name = str(input("Enter your last name: "))
        new_acct['Last Name'] = last_name
        
        while True:
            try:
                dob = input("Enter your date of birth (DD-MM-YYYY): ")
                date_of_birth = datetime.strptime(dob, "%d-%m-%Y").date()
                new_acct['Date of Birth'] = date_of_birth
                break
            except ValueError:
                print("Invalid date format! Please use DD-MM-YYYY")
                continue
        
        all_bank_accounts[new_acct['Account Number']] = {
            'Account Type': new_acct['Account Type'],
            'Account Number': new_acct['Account Number'],
            'Account Bal': new_acct['Account Bal'],
            'First Name': new_acct['First Name'],
            'Last Name': new_acct['Last Name'],
            'Date of Birth': new_acct['Date of Birth']
        }
        
        print("\nFinalizing account creation", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")
        
        print("="*50)
        print("🎉 Account Created Successfully! 🎉")
        print("="*50)
        print(f"Account Holder: {first_name} {last_name}")
        print(f"Account Type: {new_acct['Account Type']}")
        print(f"Account Number: {new_acct['Account Number']}")
        print(f"Account Bal: ${new_acct['Account Bal']}")
        print("="*50)
        
        return new_acct
    
    return None

create_account()


def debit_account():
    print("")
           
debit_account()

def credit_account():
    print("")
    
credit_account()



def close_account():
    print("")

close_account()    
    