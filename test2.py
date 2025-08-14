def check_account_info():
    display_acct = input("Kindly enter your account nummber")
    if display_acct in all_bank_accounts:
        stored_acct = all_bank_accounts[acct_num]
        print("\n📋 Account Information:")
        print("="*50)
        for key, value in stored_acct.items():
            print(f"{key}: {value}")
        print("="*50)
        
    else:
        print("Account not found. Ensure you entered the correct account number")    
    return display_acct

check_account_info()