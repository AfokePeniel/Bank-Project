from datetime import datetime
import random
import time

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