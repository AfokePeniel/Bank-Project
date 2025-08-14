from datetime import datetime
import random
import time

# In-memory "database" of accounts
all_bank_accounts = {}

# ---------------- Messages ----------------
def welcome_message():
    return "Welcome to Foxy Banking App! How can we serve you today?"

def final_greeting():
    return "Thank you for banking with us. Goodbye."

# ---------------- Utilities ----------------
def _loading(msg="Processing", dots=3, delay=0.25):
    print(f"\n{msg}", end="")
    for _ in range(dots):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()

def _require_account(acct_number: str) -> dict:
    """Fetch an account or raise a clear error."""
    acct = all_bank_accounts.get(acct_number)
    if not acct:
        raise KeyError("Account not found.")
    return acct

def generate_acct_numb(acct_type: str) -> str:
    """acct_type: 'g' (Gold), 's' (Savings), 'c' (Chequing)"""
    if acct_type == 'g':
        base = "1010"
    elif acct_type == 's':
        base = "2020"
    elif acct_type == 'c':
        base = "3030"
    else:
        raise ValueError("Invalid account type. Use 'g', 's', or 'c'.")
    suffix = "".join(str(random.randint(0, 9)) for _ in range(6))
    return base + suffix

# ---------------- Operations ----------------
def create_account():
    print("\n=== Open an Account ===")
    acct_type = input("Type ('g' Gold, 's' Savings, 'c' Chequing): ").strip().lower()
    if acct_type not in ('g', 's', 'c'):
        print("Invalid type. Please choose 'g', 's', or 'c'.")
        return

    first_name = input("First name: ").strip().title()
    last_name  = input("Last name: ").strip().title()

    # Date of birth with validation
    while True:
        dob = input("Date of birth (DD-MM-YYYY): ").strip()
        try:
            date_of_birth = datetime.strptime(dob, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    acct_number = generate_acct_numb(acct_type)
    acct_label  = "Gold" if acct_type == 'g' else "Savings" if acct_type == 's' else "Chequing"

    all_bank_accounts[acct_number] = {
        'Account Type' : acct_label,
        'Account Number': acct_number,
        'Account Bal'  : 0.0,
        'First Name'   : first_name,
        'Last Name'    : last_name,
        'Date of Birth': date_of_birth
    }

    _loading("Finalizing account creation")
    print("🎉 Account Created 🎉")
    print(f"Holder : {first_name} {last_name}")
    print(f"Type   : {acct_label}")
    print(f"Number : {acct_number}")
    print(f"Balance: ${all_bank_accounts[acct_number]['Account Bal']:.2f}")

def credit_account():
    print("\n=== Credit Account ===")
    acct_number = input("Account Number: ").strip()
    try:
        acct = _require_account(acct_number)
    except KeyError as e:
        print(e)
        return

    try:
        amount = float(input("Amount to credit: ").strip())
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    acct['Account Bal'] = float(acct.get('Account Bal', 0.0)) + amount
    _loading("Applying credit")
    print(f"✅ Credited ${amount:.2f}. New balance: ${acct['Account Bal']:.2f}")

def debit_account():
    print("\n=== Debit Account ===")
    acct_number = input("Account Number: ").strip()
    try:
        acct = _require_account(acct_number)
    except KeyError as e:
        print(e)
        return

    try:
        amount = float(input("Amount to debit: ").strip())
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    current = float(acct.get('Account Bal', 0.0))
    if current < amount:
        print("❌ Insufficient funds.")
        return

    acct['Account Bal'] = current - amount
    _loading("Processing debit")
    print(f"✅ Debited ${amount:.2f}. New balance: ${acct['Account Bal']:.2f}")

def check_account_info():
    print("\n=== Check Account ===")
    acct_number = input("Account Number: ").strip()
    try:
        acct = _require_account(acct_number)
    except KeyError as e:
        print(e)
        return

    print("-" * 50)
    print(f"Name         : {acct['First Name']} {acct['Last Name']}")
    print(f"Type         : {acct['Account Type']}")
    print(f"Number       : {acct['Account Number']}")
    print(f"Date of Birth: {acct['Date of Birth']}")
    print(f"Balance      : ${acct['Account Bal']:.2f}")
    print("-" * 50)

def close_account():
    print("\n=== Close Account ===")
    acct_number = input("Account Number: ").strip()
    if acct_number in all_bank_accounts:
        confirm = input("Type 'YES' to confirm closure: ").strip().upper()
        if confirm == "YES":
            del all_bank_accounts[acct_number]
            _loading("Closing account")
            print("✅ Account closed.")
        else:
            print("Cancelled.")
    else:
        print("Account not found.")

# ---------------- Menu ----------------
def main_menu():
    print(welcome_message())
    while True:
        print("""
Choose an option:
 1) Open an Account
 2) Credit Account
 3) Debit Account
 4) Check Account
 5) Close Account
 x) Exit
""")
        choice = input("Enter choice: ").strip().lower()

        if choice == "1":
            create_account()
        elif choice == "2":
            credit_account()
        elif choice == "3":
            debit_account()
        elif choice == "4":
            check_account_info()
        elif choice == "5":
            close_account()
        elif choice == "x":
            print(final_greeting())
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()

